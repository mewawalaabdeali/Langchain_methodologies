from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict


load_dotenv()

model = ChatOpenAI()

class Review(TypedDict):
    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""These are definitely not boyfriend jeans. They are somewhat loose skinny jeans at best. My thighs are big, but my calves aren’t, yet the thighs on these jeans are loose-ish while the calves are tight. They are midrise though and it’s so hard to find real midrise I’m willing to deal with them being skinny jeans. They are very stretchy. I ordered a 34 to be safe, but I should have ordered my usual 31-32(5’6, 220lbs). Although, if I had gone that small they probably would have ended up being true skinny jeans. The pockets are fine. I can fit my hand in but that’s about it. Honestly, if you are looking for good boyfriend jeans with pockets so deep you could hide a book in them, buy Judy Blues. These ain’t it.""")

print(result)