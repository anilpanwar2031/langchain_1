# import os
# os.environ["GOOGLE_API_KEY"] = "AIzaSyCGGvKHuk0KXygRJa4aQB77lQWD1CXm2I0"

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


# Initialize the model (e.g., "gemini-pro")
llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)

# Generate a response
response = llm.invoke("Explain quantum physics in 2 sentences.")
print(response.content)




