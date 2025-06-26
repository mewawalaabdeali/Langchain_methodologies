from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

model = ChatOpenAI()

st.header('Research Tool')

paper_input = st.selectbox("Select Research Paper name: ", ["Attention is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Lannguage Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])
style_input = st.selectbox("Select Explaination Style: ", ["Beginner-Friendly", "Technical", "Code-oriented", "Mathematical", "Theoritical story telling"])
length_input = st.selectbox("Select Explaination Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explaination)"])


template = load_prompt('template.json')


if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
    })
    
    st.write(result.content)
