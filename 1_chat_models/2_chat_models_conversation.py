from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from dotenv import load_dotenv
load_dotenv()

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3",
    temperature=0,
)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "what is 2+2"),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)


