# This program calls ChatGPT!
from langchain_openai import ChatOpenAI
import streamlit as st

# Set variables
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
myQuery = "HOW TO GET KIDS TO PAY ATTENTION?!"

# Call the LLM
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
chatResponse = llm.invoke(myQuery)

# Print output
print("Heres what ChatGPT said \n\n", chatResponse.content)
st.write(chatResponse.content)
