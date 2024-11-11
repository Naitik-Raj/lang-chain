import os
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit app
st.title("Langchain demo with OpenAI Key")
input_text = st.text_input("Write your query here...")

# Initialize OpenAI LLM with lower temperature and max_tokens
# Lower temperature and token limit
llm = OpenAI(temperature=0.3)

# Generate response if input is provided
if input_text:
    response = llm(input_text)
    st.write(response)
