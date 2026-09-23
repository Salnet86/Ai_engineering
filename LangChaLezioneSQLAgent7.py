# Installazione dei pacchetti necessari (se non già presenti)
# pip install langchain langchain-openai langchain-community sqlalchemy


import os
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.database import SQLDatabase
from langchain_openai import ChatOpenAI


# 1. Imposta la chiave API del tuo LLM (es. OpenAI)
os.environ["OPENAI_API_KEY"] = "la-tua-chiave-api"


# 2. Connessione al database (es. un database SQLite locale o altro supportato da SQLAlchemy)
# Esempio con un file SQLite: "sqlite:///database.db"
db = SQLDatabase.from_uri("sqlite:///Chinook.db")


# 3. Inizializzazione del modello linguistico
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


# 4. Creazione del toolkit SQL per permettere all'agente di interagire con lo schema
toolkit = SQLDatabaseToolkit(db=db, llm=llm)


# 5. Creazione dell'agente SQL tramite LangChain
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True, # Impostato su True per vedere i passaggi logici intermedi nel terminale
    handle_parsing_errors=True
)


# 6. Esecuzione di una query in linguaggio naturale ("Text-to-SQL")
response = agent_executor.invoke({"input": "Quanti clienti abbiamo nella tabella Customers?"})


print("Risposta dell'Agente:")
print(response["output"])

