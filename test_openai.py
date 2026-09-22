from openai import OpenAI

# Inizializza il client (legge automaticamente la variabile d'ambiente OPENAI_API_KEY)
client = OpenAI()

def chiedi_all_ia_openai(prompt_utente):
    # Chiamata al modello GPT per generare una risposta testuale
    response = client.chat.completions.create(
        model="gpt-4o-mini", # Modello efficiente e veloce di OpenAI
        messages=[
            {"role": "system", "content": "Sei un assistente AI Engineer esperto e conciso."},
            {"role": "user", "content": prompt_utente}
        ]
    )
    # Estrae il testo della risposta dalla struttura dell'oggetto di OpenAI
    return response.choices[0].message.content

if __name__ == "__main__":
    domanda = "Spiega in una frase perché l'AI Engineering è importante."
    print(f"Domanda: {domanda}\n")
    
    risposta = chiedi_all_ia_openai(domanda)
    print(f"Risposta di OpenAI:\n{risposta}")
