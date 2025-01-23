import os
import gradio as gr
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from transformers import pipeline


# Retrieve the OpenAI API key securely from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("API key not found. Please add 'OPENAI_API_KEY' as a secret in your deployment environment.")

# Initialize the OpenAI LLM - Corrected model specification
llm = ChatOpenAI(temperature=0.7, max_tokens=800, model_name="gpt-4o",  openai_api_key=OPENAI_API_KEY)

# Define the prompt template
temp = """
#Summarize the following context into a few concise key points in real-time. Focus only on essential details or actionable insights.
#Context: {context}
"""

pt = PromptTemplate(input_variables=["context"], template=temp)

# Create the LLM chain
prompt_to_gpt4 = LLMChain(llm=llm, prompt=pt)

# Speech-to-text function using Whisper
def transcript_audio(audio_file):
    try:
        pipe = pipeline("automatic-speech-recognition", model="openai/whisper-tiny.en", chunk_length_s=30)
        transcript_txt = pipe(audio_file, batch_size=8)["text"]

        # Ensure transcript_txt is a string
        if not isinstance(transcript_txt, str):
            transcript_txt = str(transcript_txt)  

        result = prompt_to_gpt4.run(transcript_txt)  # Use prompt_to_gpt4
        return result
    except Exception as e:
        # Print the error message and traceback
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return f"An error occurred: {e}" 

# Gradio interface
audio_input = gr.Audio(sources="upload", type="filepath")
output_text = gr.Textbox()

iface = gr.Interface(
    fn=transcript_audio,
    inputs=audio_input,
    outputs=output_text,
    title="Audio Transcription App",
    description="Upload the audio file"
)

iface.launch()