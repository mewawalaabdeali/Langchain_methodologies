from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

url = 'https://www.njit.edu/admissions'
model = ChatOpenAI()

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text -  \n {text}',
    input_variables=['question', 'text']
)

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'question':'Can you tell me something about the fees criteria?', 'text':docs[0].page_content}))