from google import genai

# Inizializza il client (assicurati di aver impostato la chiave API nelle variabili d'ambiente 
# come GEMINI_API_KEY, oppure passala direttamente: client = genai.Client(api_key="TUA_CHIAVE"))
client = genai.Client()

def chiedi_all_ia(prompt_utente):
    # Chiamata al modello Gemini 3.5 Flash per generare una risposta testuale
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt_utente,
    )
    return response.text

if __name__ == "__main__":
    domanda = "Spiega in una frase perché l'AI Engineering è importante."
    print(f"Domanda: {domanda}\n")
    
    risposta = chiedi_all_ia(domanda)
    print(f"Risposta dell'IA:\n{risposta}")
