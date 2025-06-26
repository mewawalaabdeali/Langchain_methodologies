from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llmodel = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task = "text-generation"
)

model = ChatHuggingFace(repo_id="HuggingFaceH4/zephyr-7b-beta", task = "text-generation")

result= model.invoke("What is the capital of United Kingdoms?")

print(result.content)