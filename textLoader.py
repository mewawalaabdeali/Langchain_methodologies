from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model = ChatAnthropic(model = 'claude-3-7-sonnet-20250219')

loader = TextLoader('cricket.txt', encoding='utf-8')
doc = loader.load()

print(doc[0].page_content)

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a summary for the following poem \n {poem}',
    input_variables=['poem']
)

chain = prompt | model | parser

print(chain.invoke({'poem':doc[0].page_content}))