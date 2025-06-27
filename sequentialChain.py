from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template='Generate a detailed report on the {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Give me 5 pointer summary of the key points from the follow text \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'Galactus and silver surfer'})

print(result)