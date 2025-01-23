import torch
import os
import gradio as gr

#from langchain.llms import OpenAI
from langchain.llms import HuggingFaceHub

from transformers import pipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

my_credentials = {
    "url"    : "https://us-south.ml.cloud.ibm.com"
}
params = {
        GenParams.MAX_NEW_TOKENS: 800, # The maximum number of tokens that the model can generate in a single run.
        GenParams.TEMPERATURE: 0.1,   # A parameter that controls the randomness of the token generation. A lower value makes the generation more deterministic, while a higher value introduces more randomness.
    }

LLAMA2_model = Model(
        model_id= 'meta-llama/llama-3-8b-instruct', 
        credentials=my_credentials,
        params=params,
        project_id="skills-network",  
        )

llm = WatsonxLLM(LLAMA2_model)  

#######------------- Prompt Template-------------####
#temp = """
#<s><<SYS>>
#List the key points with details from the context: 
#[INST] The context : {context} [/INST] 
#<</SYS>>
#"""

#temp = """
#Summarize the following context into a few concise key points in real-time. Focus only on essential details or actionable insights.
#Context: {context}
#"""

#temp = """
#You are tasked with summarizing the content of a live or recorded meeting or lecture. Your goals are:
#1. Extract and list the **key points** clearly and concisely.
#2. Highlight **decisions made**, **important ideas**, and **critical questions raised**.
#3. Exclude filler words, repetitions, and irrelevant details.
#4. Ensure the summary is presented in an **easy-to-read bullet point format**.
#5. For live events, focus on providing accurate and dynamic updates.

#Transcript: {context}
#"""

temp = """
You are assisting in summarizing a live meeting/lecture. Summarize the provided segment into concise, actionable key points. 
- Focus on main ideas, key decisions, and important details.
- Ignore filler words and minor information.
Segment: {context}
"""

# here is the simplified version of the prompt template
# temp = """
# List the key points with details from the context: 
# The context : {context} 
# """

pt = PromptTemplate(
    input_variables=["context"],
    template= temp)

prompt_to_LLAMA2 = LLMChain(llm=llm, prompt=pt)

#######------------- Speech2text-------------####

def transcript_audio(audio_file):
    # Initialize the speech recognition pipeline
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny.en",
        chunk_length_s=30,
    )
    # Transcribe the audio file and return the result
    transcript_txt = pipe(audio_file, batch_size=8)["text"]
    result = prompt_to_LLAMA2.run(transcript_txt)

    return result

#######------------- Gradio-------------####

audio_input = gr.Audio(sources="upload", type="filepath")
output_text = gr.Textbox()

iface = gr.Interface(fn= transcript_audio, 
                    inputs= audio_input, outputs= output_text, 
                    title= "Audio Transcription App",
                    description= "Upload the audio file")

iface.launch(server_name="0.0.0.0", server_port=7860)