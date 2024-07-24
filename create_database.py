from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma
import os 
import glob
import shutil
from dotenv import load_dotenv

load_dotenv()


#Set path to Chroma Database & Sources 
CHROMA_PATH = "chroma"
DATA_PATH = "data/resources"

# Main function to start the data store generation.
def main():
    generate_data_store()

# Load docs, split them into chunks and then save chuncks to Chroma DB. 
def generate_data_store():
    print("Starting to generate data store....")
    documents = load_documents() 
    chunks = split_text(documents)
    save_to_chroma(chunks)
  
# Function to load Documents from directory 
def load_documents():
    print("Loading documents from directory....")
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()

    # Print list of Markdown Files in Data directory 
    md_files = glob.glob(f"{DATA_PATH}/*.md")
    print("Markdown files found", md_files)

    print(f"Loaded{len(documents)} documents.")
    return documents

# Function to make split documents into chunks 
def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=250,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")
    document = chunks[20] #Random Chunk for Display after splitting them
    print(document.page_content)
    print(document.metadata)

    return chunks

# Saving Chunked Documents into Chroma Database 
def save_to_chroma(chunks: list[Document]):
    #clear out the database first.
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH) #Delete old DB.

    # Create a new DB from the documents.
    openai_api_key = os.getenv('OPENAI_API_KEY')
    db = Chroma.from_documents(
        chunks, OpenAIEmbeddings(openai_api_key=openai_api_key), persist_directory=CHROMA_PATH
    )
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")


if __name__ == "__main__":
    print("Calling main function...")
    main()
