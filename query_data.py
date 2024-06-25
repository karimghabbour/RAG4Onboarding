from dataclasses import dataclass
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os


# Specify Path for Chroma Database 
CHROMA_PATH = "chroma"
load_dotenv()


# Prompt template that system should follow 
PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

def query_data(query_text):
    # Prepare the DB and use same embedding function used to create it 
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Perform a similarity search in the DB using the query text
    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    # Check if no results found or if the best result has a low relevance score
    if len(results) == 0 or results[0][1] < 0.5: # Check if results are found 
        print(f"Unable to find matching results.") 
        return "Unable to find matching results.", []
    
    # Format context for the prompt 
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print(prompt)

    # Get response from the model
    model = ChatOpenAI()
    response = model.invoke(prompt)

    # Extract the actual content
    response_text = response.content  # Correct way to access the content of AIMessage

    # Collect sources
    sources = [doc.metadata.get("source", None) for doc, _score in results]
    print("---------------------------------------------------")
    print("Model Response:")
    print("---------------------------------------------------")
    print(response_text)
    print("\n" * 2)  # Add extra newlines for separation
    # Print sources
    print("---------------------------------------------------")
    print("Sources:")
    print("---------------------------------------------------")
    for source in sources:
        print(f"- {source}")
    print("\n" * 2)  # Add extra newlines for separation

    return response_text, sources

def main():
    import argparse
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text

    # Call the query_data function
    query_data(query_text)

if __name__ == "__main__":
    main()
