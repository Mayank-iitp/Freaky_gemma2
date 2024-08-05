import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACKING_V2"]="true"

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are freaky gemma, act as freky girlfield of user and answer his text"),
        ("user","Question:{question}")
    ]
)


st.title("FReaky Gemma 2: 2b hands on")
input_text=st.text_input("Hey!! ask me a question")



llm=Ollama(model="gemma2:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
