from openai import OpenAI

client = OpenAI()

def avvia_chatbot_openai():
    print("=== CHATBOT INTERATTIVO CON OPENAI (GPT) ===")
    print("Scrivi 'esci' o 'quit' per terminare la chat.\n")
    
    # Lista che memorizza la cronologia della conversazione
    cronologia_chat = [
        {"role": "system", "content": "Sei un assistente utile per un AI Engineer."}
    ]
    
    while True:
        messaggio_utente = input("Tu: ")
        if messaggio_utente.lower() in ["esci", "quit", "exit"]:
            print("Chiusura della chat. Arrivederci!")
            break
            
        if not messaggio_utente.strip():
            continue
            
        # Aggiungiamo il messaggio dell'utente alla cronologia
        cronologia_chat.append({"role": "user", "content": messaggio_utente})
        
        try:
            # Inviamo l'intera cronologia al modello per mantenere il contesto
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=cronologia_chat
            )
            
            testo_risposta = response.choices[0].message.content
            print(f"\nIA: {testo_risposta}\n" + "-"*40)
            
            # Aggiungiamo anche la risposta dell'assistente alla cronologia della chat
            cronologia_chat.append({"role": "assistant", "content": testo_risposta})
            
        except Exception as e:
            print(f"Errore durante la comunicazione: {e}")

if __name__ == "__main__":
    avvia_chatbot_openai()
  
