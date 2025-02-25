from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableSequence

from langchain_ollama import ChatOllama

model = ChatOllama(
    model="llama3",
    temperature=0,
)
