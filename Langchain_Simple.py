import streamlit as st
import os
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain



openai_key = "*********************************************" 
os.environ["OPENAI_API_KEY"] = openai_key

st.title('Langchain Demo with OpenAI')
input_text = st.text_input("Search about any Car")

first_input_prompt = PromptTemplate ( 
    input_variables =['car_name'],
    template="Give me the mileage, company and on road price in India about {car_name}"
    )
llm = OpenAI(temperature=0.8)
chain  = LLMChain(llm = llm, prompt = first_input_prompt, verbose = True)



if input_text:
    st.write(chain.run(input_text))