pip install langchain langchain-openai langchain-community psycopg2-binary python-dotenv



import os
from dotenv import load_dotenv


# Import di LangChain per i modelli, i database e gli agenti SQL
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent


# 1. CARICAMENTO DELLE VARIABILI D'AMBIENTE
load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY non trovata nel file .env")




# ==========================================
# 2. CONFIGURAZIONE DELLA CONNESSIONE AL DATABASE
# ==========================================
# Stringa di connessione PostgreSQL (Modifica con i tuoi parametri reali)
# Formato: postgresql://utente:password@host:porta/nome_database
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "tuo_database")


db_uri = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


# Inizializzazione del wrapper SQLDatabase di LangChain
db = SQLDatabase.from_uri(db_uri)




# ==========================================
# 3. INIZIALIZZAZIONE DEL MODELLO LLM
# ==========================================
# Utilizziamo GPT-4o-mini con temperatura a 0 per garantire risposte deterministiche sulle query
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)




# ==========================================
# 4. CREAZIONE DELL'AGENTE SQL
# ==========================================
# create_sql_agent combina automaticamente il modello, gli strumenti per analizzare lo schema
# e il toolkit per eseguire query SQL in sicurezza sul database connesso.
sql_agent_executor = create_sql_agent(
    llm=llm,
    db=db,
    agent_type="tool-calling", # Tipo di agente basato sull'uso dei tool nativi dei modelli
    verbose=True # Mostra nel terminale i passaggi intermedi (pensiero, query generata, risultato)
)




# ==========================================
# 5. ESECUZIONE DI UNA RICHIESTA IN LINGUAGGIO NATURALE
# ==========================================
if __name__ == "__main__":
    # Esempio di domanda in linguaggio naturale rivolta al database
    user_query = "Quanti clienti abbiamo registrati nella tabella clienti?"
    
    print(f"Domanda dell'utente: {user_query}\n")
    
    # Esecuzione dell'agente
    response = sql_agent_executor.invoke({"input": user_query})
    
    print("\nRisposta finale dell'agente:")
    print(response["output"])

