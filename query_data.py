from dataclasses import dataclass
from langchain_community.vectorstores import Chroma
#from langchain_openai import OpenAIEmbeddings -> no need anymore
#from langchain_openai import ChatOpenAI -> no need anymore 
#from langchain.prompts import ChatPromptTemplate -> no need anymore 
from dotenv import load_dotenv
import os
from get_chat_model import get_chat_model
from get_embedding_function import get_embedding_function
from transformers import AutoTokenizer, AutoModelForCausalLM




# Specify Path for Chroma Database 
CHROMA_PATH = "chroma"
#load_dotenv() -> no need for API key anymore


# Prompt template that system should follow 
PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

def query_data(query_text):
    # Prepare the DB and use same embedding function used to create it 
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Perform a similarity search in the DB using the query text
    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    # Check if no results found or if the best result has a low relevance score
    if len(results) == 0 or results[0][1] < 0.5: # Check if results are found 
        print(f"Unable to find matching results.") 
        return "Unable to find matching results.", []
    
    # Format context for the prompt 
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt = PROMPT_TEMPLATE.format(context=context_text, question=query_text)
    print(prompt)

    # Get tokenizer and model
    tokenizer, model = get_chat_model()

    # Tokenize input
    inputs = tokenizer(prompt, return_tensors='pt')

    # Generate response
    outputs = model.generate(**inputs)
    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

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
