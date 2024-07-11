from langchain_community.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores.chroma import Chroma
import glob
import argparse
import shutil
import os
from get_embedding_function import get_embedding_function

def main():
    # Check if the database should be cleared (using the --clear flag)
    # Create the argument parser to handle command-line arguments
    parser = argparse.ArgumentParser()
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

DATA_PATH = "data/resources"
CHROMA_PATH = "chroma"

def load_documents():
    print("Loading PDFs from directory....")
    pdf_loader = PyPDFDirectoryLoader(DATA_PATH, glob="*.pdf")
    pdf_documents = pdf_loader.load()
    pdf_files = glob.glob(f"{DATA_PATH}/*.[pP][dD][fF]")
    print(f"{len(pdf_files)} PDF files found: {pdf_files}")
    print(f"Loaded {len(pdf_files)} Pages of PDF documents.")

    print("\n" * 2)
    print("Loading .md files from directory....")
    md_loader = DirectoryLoader(DATA_PATH, glob="*.md")
    md_documents = md_loader.load()
    md_files = glob.glob(f"{DATA_PATH}/*.md")
    print(f"{len(md_files)} Markdown files found: {md_files}")
    print(f"Loaded {len(md_documents)} Markdown documents.")
    
    documents = pdf_documents + md_documents 
    print("\n" * 2)
    print(f"Loaded {len(documents)} documents of all types.")
    return documents

def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split into {len(chunks)} chunks.")
    return chunks

def add_to_chroma(chunks: list[Document]):
    embedding_function = get_embedding_function()
    db = Chroma(
        persist_directory=CHROMA_PATH, embedding_function=embedding_function
    )
    chunks_with_ids = calculate_chunk_ids(chunks)
    existing_items = db.get(include=[])
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing documents in DB: {len(existing_items)}")

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
    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id
        chunk.metadata["id"] = chunk_id
        #print(f"Assigned chunk ID: {chunk_id}")

    return chunks

def clear_database():
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

if __name__ == "__main__":
    main()
