from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate([
    ('system', 'You are a very helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

chat_history=[]

with open('chat-history.txt') as f:
    chat_history.extend(f.readLines())

print(chat_history)

prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

print(prompt)