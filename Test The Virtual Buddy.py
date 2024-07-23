import streamlit as st
from query_data import query_data  # Import the query_data function
from PIL import Image

def format_response(response_text, sources):
    # Format the response
    formatted_response = f"### Model Response\n\n{response_text}\n\n"
    formatted_sources = "### Sources\n\n" + "\n".join([f"- {source}" for source in sources if source])
    return formatted_response, formatted_sources

st.set_page_config(page_title="HPE Barcelona Virtual Buddy", page_icon=":sunglasses:", layout="wide")


# Title of the app
st.title("HPE Barcelona Virtual Buddy")
st.header("Welcome! You can ask me anything and I will do my best to help you")




# Input for the user query
user_query = st.text_input("Enter your question:")


# Button to submit the query
if st.button("Submit"):
    if user_query:
        # Query the RAG system
        response, sources = query_data(user_query)  # Call the query function
        
        # Format the response and sources
        formatted_response, formatted_sources = format_response(response, sources)
        
        # Display the response
        st.markdown(formatted_response)
        st.markdown(formatted_sources)
    else:
        st.write("Please enter a question.")


cover = Image.open("images/HPE.jpg")
st.image(cover, use_column_width=True)
