from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=15)
# Use case of temperature
#Factual Answers (mode, code, facts) -- 0.0 - 0.3
#Balanced response(general QA, explainations) -- 0.5 - 0.7
#Creative writing, storytelling, jokes -- 0.9 - 1.2
#Maximum randomness(wild ideas, brainstorming) -- 1.5+

result = model.invoke("Write a 5 line poem on cricket.")

print(result.content)