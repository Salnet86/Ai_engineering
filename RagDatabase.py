from google import genai
import chromadb

client = genai.Client()

# 1. Inizializziamo un database vettoriale locale (salvato in memoria o su disco)
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="miei_documenti")

# 2. Simuliamo il caricamento di un file di testo e lo dividiamo in "pezzi" (chunks)
testo_documento = """
Il corso IFTS Dalì copre argomenti di informatica avanzata e programmazione.
L'AI Engineering richiede la conoscenza di Python, delle API e dei sistemi di orchestrazione.
I database vettoriali memorizzano i dati sotto forma di embedding numerici basati sul significato semantico.
"""
chunks = [chunk.strip() for chunk in testo_documento.strip().split("\n") if chunk.strip()]

# 3. Creiamo gli embedding per ogni pezzo usando il modello di Google e li carichiamo nel DB
print("Indicizzazione dei documenti nel database vettoriale...")
for i, chunk in enumerate(chunks):
    # Generiamo l'embedding con l'API di Gemini
    response_emb = client.models.embed_content(
        model="text-embedding-004",
        contents=chunk
    )
    vector = response_emb.embeddings[0].values
    
    # Salviamo nel database vettoriale
    collection.add(
        documents=[chunk],
        embeddings=[vector],
        ids=[str(i)]
    )

def query_rag_avanzato(domanda_utente):
    # 4. Generiamo l'embedding della domanda dell'utente
    query_emb = client.models.embed_content(
        model="text-embedding-004",
        contents=domanda_utente
    )
    query_vector = query_emb.embeddings[0].values
    
    # 5. Cerchiamo nel database vettoriale i pezzi più simili semanticamente
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=1 # Prende il pezzo più rilevante
    )
    
    contesto_trovato = results['documents'][0][0]
    print(f"\n[Contesto trovato nel DB]: {contesto_trovato}")
    
    # 6. Chiediamo a Gemini di rispondere basandosi solo su quel contesto
    prompt = f"Usa questo contesto per rispondere alla domanda: {contesto_trovato}\n\nDomanda: {domanda_utente}"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    domanda = "Cosa memorizzano i database vettoriali?"
    print(f"Domanda: {domanda}")
    risposta = query_rag_avanzato(domanda)
    print(f"\nRisposta IA:\n{risposta}")
          
