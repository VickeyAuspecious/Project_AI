import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
# load_dotenv()
API_KEY = "AIzaSyCDOwPq7kOMbCoZcZZ8Xx8bJC6xLjPlSDE"
genai.configure(api_key=os.getenv("API_KEY"))
st.title("Generative AI Search")
st.write("Enter your query and let AI assist you!")
inputtxt = st.text_input("Enter what you wanna search:")

if st.button("Search"):
    if inputtxt:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(inputtxt)
        
        st.write("### AI Response:")
        st.write(response.text)
    else:
        st.write("Please enter a valid query.")






