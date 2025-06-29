from langchain_community.document_loaders import DirectoryLoader, CSVLoader

loader = DirectoryLoader(
    path='Documents',
    glob='*.csv',
    loader_cls=CSVLoader
)

docs = loader.load()

print(len(docs))