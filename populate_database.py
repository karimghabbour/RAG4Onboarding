from langchain_community.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_community.document_loaders import DirectoryLoader
import glob
import argparse
import shutil
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from dotenv import load_dotenv
import os
from get_embedding_function import get_embedding_function
from langchain_community.vectorstores.chroma import Chroma
from langchain.schema import Document


def main():
    # Check if the database should be cleared (using the --clear flag).
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    args = parser.parse_args()
    if args.reset:
        print("✨ Clearing Database")
        clear_database()

    # Create (or update) the data store.
    documents = load_documents()
    chunks = split_documents(documents)
    chunks_with_ids = calculate_chunk_ids(chunks)
    add_to_chroma(chunks_with_ids)




#Loading documents from inside data folder
DATA_PATH = "data/resources"

def load_documents():
    #Load PDFs
    print("Loading PDFs from directory....")
    pdf_loader = PyPDFDirectoryLoader(DATA_PATH, glob="*.pdf")
    pdf_documents = pdf_loader.load()
    # Print list of PDF Files in Folder
    pdf_files = glob.glob(f"{DATA_PATH}/*.pdf")
    print("PDF files found", pdf_files)
    print(f"Loaded {len(pdf_documents)} PDF documents.")

    #Load md Files
    print("Loading .md files from directory....")
    md_loader = DirectoryLoader(DATA_PATH, glob="*.md")
    md_documents = md_loader.load()
    # Print list of .md Files in Folder
    md_files = glob.glob(f"{DATA_PATH}/*.md")
    print("Markdown files found", md_files)
    print(f"Loaded {len(md_documents)} Markdown documents.")
    
    #Combine both lists 
    documents = pdf_documents + md_documents 
    print(f"Loaded {len(documents)} documents of all types.")
    return documents

#TESTING
#To check out the loaded documents
#documents = load_documents()
#print("\n" * 2)  # Add extra newlines for separation
#print(documents[0])

# Splitting Documents into Chunks
def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)

#TESTING
#To check out the chunks 
#documents = load_documents()
#chunks = split_documents(documents)
#print("\n" * 2)  # Add extra newlines for separation
#print("Chunks:","\n"*2, chunks[0])

CHROMA_PATH = "chroma"

def add_to_chroma(chunks: list[Document]):
    # Load the existing database.
    db = Chroma(
        persist_directory=CHROMA_PATH, embedding_function=get_embedding_function()
    )

    # Calculate Page IDs.
    chunks_with_ids = calculate_chunk_ids(chunks)

    # Add or Update the documents.
    existing_items = db.get(include=[])  # IDs are always included by default
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing documents in DB: {len(existing_ids)}")

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

    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        # If the page ID is the same as the last one, increment the index.
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        # Calculate the chunk ID.
        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id

        # Add it to the page meta-data.
        chunk.metadata["id"] = chunk_id

    return chunks


def clear_database():
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

if __name__ == "__main__":
    main()