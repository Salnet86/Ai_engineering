# Installazione: pip install openai (Le API di Perplexity sono compatibili con il client OpenAI)
from openai import OpenAI

# Perplexity usa lo stesso standard di OpenAI ma con il suo endpoint e la sua chiave
client = OpenAI(
    api_key="TUA_chiave_PERPLEXITY",
    base_url="https://api.perplexity.ai"
)

def cerca_con_perplexity(domanda):
    print(f"Interrogazione del motore di ricerca IA per: '{domanda}'...\n")
    
    response = client.chat.completions.create(
        model="sonar", # Modello ottimizzato per la ricerca web in tempo reale
        messages=[
            {"role": "system", "content": "Sei un assistente di ricerca preciso. Fornisci risposte dettagliate e citi le fonti quando possibile."},
            {"role": "user", "content": domanda}
        ]
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    risultato = cerca_con_perplexity("Quali sono le ultime novità sull'intelligenza artificiale?")
    print(risultato)
  
