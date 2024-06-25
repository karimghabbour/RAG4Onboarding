from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

#Create Embedding function
def get_embedding_function():
    load_dotenv()
    openai_api_key = os.getenv('OPENAI_API_KEY')
    embeddings =  OpenAIEmbeddings(openai_api_key=openai_api_key)
    return embeddings
