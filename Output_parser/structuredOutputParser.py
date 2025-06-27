from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)

schema = [
    ResponseSchema(name = 'fact1', description="Fact1 about the topic"),
    ResponseSchema(name = 'fact2', description="Fact2 about the topic"),
    ResponseSchema(name = 'fact3', description="Fact3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='You are a JSON generator. Give me 3 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)

chain = template | model | parser

result = chain.invoke({'topic':'Kubecon'})

print(result)