import streamlit as st
import os
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain 


openai_key = "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" 
os.environ["OPENAI_API_KEY"] = openai_key

st.title('Langchain Demo with OpenAI')
input_text = st.text_input("Search about any Car")

first_input_prompt = PromptTemplate ( 
    input_variables =['car_name'],
    template="Give me the mileage about {car_name}. Strictly give the numbers only. Do not give any explanations."
    )
llm = OpenAI(temperature=0.8)
chain  = LLMChain(llm = llm, prompt = first_input_prompt, verbose = True, output_key ='Mileage')


second_input_prompt = PromptTemplate ( 
    input_variables =['Mileage'],
    template="Give me the manufacturing company of {Mileage}"
    )

chain2 = LLMChain(llm = llm, prompt = second_input_prompt, verbose=True, output_key="Company Name")

parent_chain  = SequentialChain(
    chains=[chain,chain2],input_variables = ['car_name'], output_variables = ['Mileage','Company Name'],verbose=True)

if input_text:
    st.write(parent_chain({'car_name':input_text}))