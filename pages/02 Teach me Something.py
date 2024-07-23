import streamlit as st
import pandas as pd

#we are using the same df from the page 01. Sometimes is better to save functions to avoid mixing up and repetitions, see?
st.set_page_config(page_title="Teacher", page_icon=":cinema:", layout="wide")

st.title("Teach our model new information")

st.header("This part of the model will allow the user to input new information to the model")
#there are a lot of inputs from the user, from Text to Dataframes and images. Use it wisely in your project!
teacher = st.text_input("Teach me something")

# Count the number of times the word appears in the "Line" column. That is the script!

