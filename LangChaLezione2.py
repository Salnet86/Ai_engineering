import os
from dotenv import load_dotenv


load_dotenv() # carica le variabili d'ambiente dal file .env


groq_api_key = os.getenv("GROQ_API_KEY")


if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set. Please check your .env")


from langchain_groq import ChatGroq


llm = ChatGroq(
    api_key=groq_api_key,
    model="llama3-8b-8192"
)


result = llm.invoke("What is the national game of India?")


print(result.content)

