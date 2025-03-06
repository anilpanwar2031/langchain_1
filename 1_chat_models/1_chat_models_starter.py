# import os
# os.environ["GOOGLE_API_KEY"] = "AIzaSyCGGvKHuk0KXygRJa4aQB77lQWD1CXm2I0"

from dotenv import load_dotenv
load_dotenv()

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3",
    temperature=0,
)

# Generate a response
response = llm.invoke("Explain quantum physics in 2 sentences.")
print(response.content)




