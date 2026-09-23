import os
from typing import List, Optional
from dotenv import load_dotenv
from pydantic import BaseModel, Field


# Import dei componenti LangChain per i modelli OpenAI
from langchain_openai import ChatOpenAI


# 1. CARICAMENTO DELLE VARIABILI D'AMBIENTE
load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY non trovata nel file .env")




# ==========================================
# 2. DEFINIZIONE DELLO SCHEMA CON PYDANTIC
# ==========================================
# Questo schema definisce esattamente la struttura e i tipi di dati
# che vogliamo ricevere in risposta dal modello LLM.
class ProductReviewAnalysis(BaseModel):
    product_name: str = Field(description="Nome del prodotto recensito")
    sentiment: str = Field(description="Sentimento generale: Positivo, Neutro o Negativo")
    key_features_mentioned: List[str] = Field(description="Elenco delle caratteristiche principali menzionate")
    rating_out_of_5: float = Field(description="Valutazione stimata da 1 a 5 basata sul testo")
    summary: str = Field(description="Breve riassunto della recensione")




# ==========================================
# 3. INIZIALIZZAZIONE DEL MODELLO E STRUTTURAZIONE
# ==========================================
# Inizializziamo il modello di chat OpenAI
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


# Colleghiamo il modello allo schema Pydantic usando .with_structured_output()
# Questo forza l'LLM a restituire un oggetto conforme esattamente allo schema definito sopra.
structured_llm = llm.with_structured_output(ProductReviewAnalysis)




# ==========================================
# 4. ESECUZIONE DELLA CHIAMATA AL MODELLO
# ==========================================
if __name__ == "__main__":
    # Testo di esempio (es. una recensione di un utente)
    review_text = (
        "Ho acquistato lo Smartwatch X200 settimana scorsa. La durata della batteria è eccezionale, "
        "dura quasi una settimana intera con un uso intenso! Il display AMOLED è luminoso e si vede "
        "benissimo anche sotto la luce del sole. Peccato solo che il cinturino in dotazione sia un po' "
        "rigido e scomodo, ma per il prezzo pagato sono davvero molto soddisfatto. Voto 4.5 su 5."
    )


    print(f"Testo di input:\n{review_text}\n")
    print("Elaborazione in corso con output strutturato...")


    # Richiesta al modello strutturato
    result: ProductReviewAnalysis = structured_llm.invoke(
        f"Analizza la seguente recensione e restituisci i dati strutturati:\n\n{review_text}"
    )


    # Stampa del risultato tipizzato (ritorna un oggetto Pydantic, non una semplice stringa)
    print("\nRisultato strutturato ottenuto (Oggetto Pydantic):")
    print(f"Prodotto : {result.product_name}")
    print(f"Sentimento : {result.sentiment}")
    print(f"Caratteristiche : {result.key_features_mentioned}")
    print(f"Voto : {result.rating_out_of_5}/5")
    print(f"Riassunto : {result.summary}")
    
    # È possibile anche convertirlo facilmente in dizionario o JSON
    print("\nFormato JSON:")
    print(result.model_dump_json(indent=2))

