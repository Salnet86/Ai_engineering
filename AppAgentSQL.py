import os
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv


# Caricamento delle variabili d'ambiente (chiave API di Groq dal file .env)
load_dotenv()


# 1. Connessione al database SQLite tramite URI di SQLAlchemy
db = SQLDatabase.from_uri("sqlite:///bank.db")


# 2. Inizializzazione del Large Language Model tramite Groq (es. Llama 3.3)
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


# 3. Creazione dell'agente SQL con LangChain
agent_executor = create_sql_agent(
    llm=llm,
    db=db,
    agent_type="tool-calling-agent",
    verbose=True # Mostra nel terminale i passaggi di ragionamento e le query generate
)


# 4. Esecuzione di una domanda in linguaggio naturale (Text-to-SQL)
response = agent_executor.invoke({
    "input": "Quanti prestiti di tipo personal sono stati erogati?"
})


print("\nRisposta Finale dell'Agente:")
print(response["output"])

