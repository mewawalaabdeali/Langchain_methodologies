from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

loader = PyPDFLoader('Documents\SignExplainer_An_Explainable_AI-Enabled_Framework_.pdf')
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 250,
    chunk_overlap = 15,
    separator=''
)

result = splitter.split_documents(docs)
print(result[0].page_content)