from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# 1. Colleghiamo gli embedding e apriamo il nostro database Chroma esistente
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = Chroma(persist_directory="./db_chroma", embedding_function=embeddings)

# Creiamo il "retriever" (il cercatore che scandaglia il database)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3}) 

# 2. Definiamo il Prompt Template (le istruzioni fisse per il modello)
template = """Sei un assistente tecnico esperto. Rispondi alla domanda usando SOLO il contesto fornito qui sotto. 
Se non trovi la risposta nel contesto, di' chiaramente che non la conosci.

Contesto:
{context}

Domanda: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

# 3. Inizializziamo il Modello LLM (il "cervello" generativo)
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Funzione di servizio per formattare i documenti estratti in un unico testo
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# 4. Cablaggio della Chain (Il circuito logico con l'operatore "|")
chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

# --- ACCENSIONE DEL SISTEMA ---
# Facciamo una domanda al nostro sistema RAG
risposta = chain.invoke("Quali pin gestiscono l'alimentazione della centralina?")
print(risposta)
