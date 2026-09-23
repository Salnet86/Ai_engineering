from langchain_chroma import Chroma
from langchain_community.embeddings import OllamaEmbeddings  # Embedding gratuiti in locale
from langchain_community.chat_models import ChatOllama        # Modello Llama in locale
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# 1. Usiamo Ollama anche per calcolare gli embedding (gratuitamente sul PC)
embeddings = OllamaEmbeddings(model="llama3")

# Apriamo il database Chroma in locale
vectorstore = Chroma(persist_directory="./db_chroma", embedding_function=embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 2. Il Prompt Template (le istruzioni per il modello)
template = """Sei un assistente tecnico esperto. Rispondi alla domanda usando SOLO il contesto fornito qui sotto. 
Se non trovi la risposta nel contesto, di' chiaramente che non la conosci.

Contesto:
{context}

Domanda: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

# 3. Inizializziamo il modello LLM locale (Llama 3 che gira con Ollama)
model = ChatOllama(model="llama3", temperature=0)

# Funzione per formattare i documenti estratti
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# 4. Cablaggio della Chain (Identica a prima, con l'operatore "|")
chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

# --- ACCENSIONE DEL SISTEMA IN LOCALE ---
risposta = chain.invoke("Quali pin gestiscono l'alimentazione della centralina?")
print(risposta)
