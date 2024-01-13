import streamlit as st
import os
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

from langchain.chains import SimpleSequentialChain


openai_key = "********************************************" 
os.environ["OPENAI_API_KEY"] = openai_key

st.title('Langchain Demo with OpenAI')
input_text = st.text_input("Search about any Car")

first_input_prompt = PromptTemplate ( 
    input_variables =['car_name'],
    template="Give me the mileage, company and on road price in India about {car_name}"
    )
llm = OpenAI(temperature=0.8)
chain  = LLMChain(llm = llm, prompt = first_input_prompt, verbose = True, output_key ='answer1')


second_input_prompt = PromptTemplate ( 
    input_variables =['answer1'],
    template="Give me the mileage, company details of {answer1} of similar type"
    )

chain2 = LLMChain(llm = llm, prompt = second_input_prompt, verbose=True)

# parent_chain  = SimpleSequentialChain(chains=[chain,chain2],verbose=True)
parent_chain  = SimpleSequentialChain(
    chains=[chain,chain2],verbose=True)

if input_text:
    st.write(parent_chain.run(input_text))