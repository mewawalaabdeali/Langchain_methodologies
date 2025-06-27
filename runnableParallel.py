from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel, RunnableSequence

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Generate a tweet about the {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='Generate a linkedIn post about the {topic}',
    input_variables=['topic']
)

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedIn': RunnableSequence(prompt2, model, parser)

})

result = parallel_chain.invoke({'topic':'AI taking the world to dystopian era'})

print(result)