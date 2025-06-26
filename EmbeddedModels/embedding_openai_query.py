from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

result  = embeddings.embed_query("London is the capital of United Kingdoms")

print(str(result))