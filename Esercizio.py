# Schema logico di un Mini-Perplexity artigianale con Python
def mini_perplexity_flow(domanda_utente):
    # STEP 1: Simuliamo di aver cercato sul web e trovato dei risultati con le fonti
    fonti_web_trovate = [
        {"url": "https://sito-tech.it/articolo-1", "testo": "L'AI Engineering sta crescendo del 40% nelle aziende europee."},
        {"url": "https://notizie-software.com/post", "testo": "I framework come LangChain e LlamaIndex sono i più usati per integrare i dati."}
    ]
    
    # Uniamo i testi delle fonti in un unico contesto
    contesto_unito = "\n\n".join([f"Fonte [{f['url']}]: {f['testo']}" for f in fonti_web_trovate])
    
    # STEP 2: Creiamo il prompt di istruzione per l'IA
    prompt_finale = f"""
Agisci come un motore di ricerca stile Perplexity. Rispondi alla domanda dell'utente usando le informazioni delle fonti fornite qui sotto. 
Per ogni affermazione chiave, inserisci il link della fonte tra parentesi quadre (es. [URL]).

FONTI WEB:
{contesto_unito}

DOMANDA:
{domanda_utente}
"""
    
    # STEP 3: Inviamo tutto al modello (es. Gemini o GPT)
    # response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt_finale)
    # return response.text
    
    print("Prompt generato pronto per l'invio al modello con allegate le fonti web.")

if __name__ == "__main__":
    mini_perplexity_flow("Quali framework sono i più usati nell'AI?")
