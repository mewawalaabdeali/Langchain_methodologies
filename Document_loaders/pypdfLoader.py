from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Research_Paper.pdf')

docs = loader.load()


#pdf loader link : https://python.langchain.com/docs/concepts/document_loaders/
#There are various pdf loaders available based on different use case, refer the link to use most appropriate.

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)