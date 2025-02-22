import os
import torch
from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.llms import HuggingFaceHub
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes, DecodingMethods
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models import Model

from langchain import PromptTemplate
#from langchain.chains import LLMChain, SimpleSequentialChain

# Check for GPU availability and set the appropriate device for computation.
DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"

#watsonx_API = " "  # Replace with your actual API key
#project_id = " "  # Replace with your actual project ID


# Global variables
conversation_retrieval_chain = None
chat_history = []
llm_hub = None
embeddings = None

# Function to initialize the language model and its embeddings
def init_llm():
    global llm_hub, embeddings

    my_credentials = {
        #"apikey": watsonx_API,
        "url"    : "https://us-south.ml.cloud.ibm.com"
    }


    params = {
            GenParams.MAX_NEW_TOKENS: 256, # The maximum number of tokens that the model can generate in a single run.
            GenParams.TEMPERATURE: 0.1,   # A parameter that controls the randomness of the token generation. A lower value makes the generation more deterministic, while a higher value introduces more randomness.
        }


    LLAMA2_model = Model(
            model_id= 'meta-llama/llama-3-8b-instruct', 
            credentials=my_credentials,
            params=params,
            project_id="skills-network"
            )



    llm_hub = WatsonxLLM(model=LLAMA2_model)

    ### --> if you are using huggingFace API:
    # Set up the environment variable for HuggingFace and initialize the desired model, and load the model into the HuggingFaceHub
    # dont forget to remove llm_hub for watsonX

    # os.environ["HUGGINGFACEHUB_API_TOKEN"] = "YOUR API KEY"
    # model_id = "tiiuae/falcon-7b-instruct"
    #llm_hub = HuggingFaceHub(repo_id=model_id, model_kwargs={"temperature": 0.1, "max_new_tokens": 600, "max_length": 600})

    #Initialize embeddings using a pre-trained model to represent the text data.
    embeddings = HuggingFaceInstructEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={"device": DEVICE}
    )


# Function to process a PDF document
def process_document(document_path):
    global conversation_retrieval_chain

    # Load the document
    loader = PyPDFLoader(document_path)
    documents = loader.load()

    # Split the document into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=64)
    texts = text_splitter.split_documents(documents)

    # Create an embeddings database using Chroma from the split text chunks.
    db = Chroma.from_documents(texts, embedding=embeddings)


    # --> Build the QA chain, which utilizes the LLM and retriever for answering questions. 
    # By default, the vectorstore retriever uses similarity search. 
    # If the underlying vectorstore support maximum marginal relevance search, you can specify that as the search type (search_type="mmr").
    # You can also specify search kwargs like k to use when doing retrieval. k represent how many search results send to llm
    conversation_retrieval_chain = RetrievalQA.from_chain_type(
        llm=llm_hub,
        chain_type="stuff",
        retriever=db.as_retriever(search_type="mmr", search_kwargs={'k': 6, 'lambda_mult': 0.25}),
        return_source_documents=False,
        input_key = "question"
     #   chain_type_kwargs={"prompt": prompt} # if you are using prompt template, you need to uncomment this part
    )


# Function to process a user prompt
def process_prompt(prompt):
    global conversation_retrieval_chain
    global chat_history

    # Query the model
    output = conversation_retrieval_chain({"question": prompt, "chat_history": chat_history})
    answer = output["result"]

    # Update the chat history
    chat_history.append((prompt, answer))

    # Return the model\'s response
    return answer

# Initialize the language model
init_llm()
