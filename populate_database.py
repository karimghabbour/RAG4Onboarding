from langchain_community.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from get_embedding_function import get_embedding_function
from langchain_community.vectorstores.chroma import Chroma
import glob
import argparse
import shutil
import os
from dotenv import load_dotenv

def main():
    # Check if the database should be cleared (using the --clear flag) + Create the argument parser to handle command-line arguments
    parser = argparse.ArgumentParser()
    # Add a reset argument that clears the database when it sees --reset
    # python populate_database.py --reset
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    args = parser.parse_args()
    if args.reset:
        print("✨ Clearing Database")
        clear_database()

    # Create (or update) the data store.
    documents = load_documents()  # Calls load documents function
    if not documents:
        print("No documents loaded. Exiting...")
        return

    chunks = split_documents(documents)  # Splits loaded docs
    if not chunks:
        print("No chunks created. Exiting...")
        return

    chunks_with_ids = calculate_chunk_ids(chunks)  # Assigns Ids to all chunks
    add_to_chroma(chunks_with_ids)  # Adds the processed chunks to Chroma DB

    # Testing: Print loaded documents
    # Uncomment the following lines to test
    # print("\n" * 2)  # Add extra newlines for separation
    # print(documents[0])

    # Testing: Print the first chunk
    # Uncomment the following lines to test
    # print("\n" * 2)  # Add extra newlines for separation
    # print("First chunk:", "\n" * 2, chunks[0])

# Loading documents from inside data folder & Specifying Chroma Path
DATA_PATH = "data/resources"
CHROMA_PATH = "chroma"

def load_documents():
    # Function to load files
    print("Loading PDFs from directory....")
    pdf_loader = PyPDFDirectoryLoader(DATA_PATH, glob="*.pdf")
    pdf_documents = pdf_loader.load()
    # Print list of PDF Files in Folder
    pdf_files = glob.glob(f"{DATA_PATH}/*.[pP][dD][fF]")
    print(f"{len(pdf_files)} PDF files found: {pdf_files}")
    print(f"Loaded {len(pdf_documents)} Pages of PDF documents.")

    # Load Markdown Files
    print("\n" * 2)  # Add extra newlines for separation
    print("Loading .md files from directory....")
    md_loader = DirectoryLoader(DATA_PATH, glob="*.md")
    md_documents = md_loader.load()
    # Print list of Markdown Files in Folder
    md_files = glob.glob(f"{DATA_PATH}/*.md")
    # print("Markdown files found", md_files)
    print(f"{len(md_files)} Markdown files found: {md_files}")
    print(f"Loaded {len(md_documents)} Markdown documents.")
    
    # Combine both lists 
    documents = pdf_documents + md_documents 
    print("\n" * 2)  # Add extra newlines for separation
    print(f"Loaded {len(documents)} documents of all types.")
    return documents

def split_documents(documents: list[Document]):
    # Splitting Documents into Chunks with RecursiveCharacterTextSplitter -> a class used to split text documents into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,  # len = length will be measured in characters (could be "words" or other metrics)
        is_separator_regex=False,  # if false then separators are simple patterns, like space comma etc
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Splitted into {len(chunks)} chunks.")
    return chunks

def add_to_chroma(chunks: list[Document]):
    # Load the existing database + calls the embedding function
    db = Chroma(
        persist_directory=CHROMA_PATH, embedding_function=get_embedding_function()
    )

    # Call chunks ID function to assign ID to each chunk 
    chunks_with_ids = calculate_chunk_ids(chunks)

    # Add or Update the documents.
    existing_items = db.get(include=[])  # IDs are always included by default
    existing_ids = set(existing_items["ids"]) # Extract and store the IDs of existing documents.
    print(f"Number of existing documents in DB: {len(existing_items)}")

    # Only add documents that don't exist in the DB.
    new_chunks = []
    for chunk in chunks_with_ids:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)

    if len(new_chunks):
        print(f"👉 Adding new documents: {len(new_chunks)}")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids=new_chunk_ids)
        db.persist()
    else:
        print("✅ No new documents to add")

def calculate_chunk_ids(chunks):
    # This will create IDs like "data/monopoly.pdf:6:2"
    # Page Source : Page Number : Chunk Index
    last_page_id = None #Keeps track of the ID of the last processed page.
    current_chunk_index = 0 #Keeps track of the index of the current chunk on a page.

    for chunk in chunks:
        #Loop through each chunk and get the source and page from its metadata.
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        #Construct current_page_id using source and page.
        current_page_id = f"{source}:{page}"

        # If the page ID is the same as the last one, increment the index.
        if current_page_id == last_page_id:
            current_chunk_index += 1 #If the current_page_id is the same as the last one, increment the chunk index.
        else:
            current_chunk_index = 0 #If it is different, reset the chunk index to 0.

        chunk_id = f"{current_page_id}:{current_chunk_index}" #Create a unique chunk_id using the current_page_id and current_chunk_index.
        last_page_id = current_page_id #Update the last_page_id.
        chunk.metadata["id"] = chunk_id  # Add the chunk_id to the chunk’s metadata.
        print(f"Assigned chunk ID: {chunk_id}")

    return chunks

def clear_database():
    #Function to remove Existing Chroma DB
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

if __name__ == "__main__":
    main()
