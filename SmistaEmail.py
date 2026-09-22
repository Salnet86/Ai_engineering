from google import genai
import json

client = genai.Client()

def smista_email(testo_email: str) -> str:
    """Analizza il testo di un'email ricevuta, la classifica e restituisce un'azione e un riassunto."""
    
    prompt = f"""
Sei un assistente AI per il customer service aziendale. Analizza l'email ricevuta e restituisci un oggetto JSON con questi campi esatti:
- "categoria": scegli tra [Fatturazione, Supporto Tecnico, Commerciale, Altro]
- "urgenza": scegli tra [Alta, Media, Bassa]
- "azione_consigliata": cosa deve fare l'azienda (es. "Inoltra al reparto amministrativo", "Rispondi con procedura di reso", ecc.)
- "bozza_risposta": una breve bozza di risposta cortese per il cliente.

EMAIL RICEVUTA:
\"\"\"{testo_email}\"\"\"
"""

    # Usiamo il modello per generare la classificazione strutturata
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json" # Forza il modello a rispondere rigorosamente in formato JSON
        }
    )
    
    return response.text

if __name__ == "__main__":
    # Esempio di email in arrivo da un cliente
    email_ricevuta = """
    Buongiorno, vi scrivo perché non riesco a visualizzare la fattura del mese scorso nel mio pannello di controllo. 
    Inoltre il servizio è rimasto bloccato per due ore stamattina. Potete risolvermi il problema urgentemente? 
    Il mio codice cliente è CL-9928.
    """
    
    print("=== ANALISI E SMISTAMENTO EMAIL IN CORSO ===")
    print(f"Testo email:\n{email_ricevuta}\n")
    
    risultato_json = smista_email(email_ricevuta)
    
    # Stampiamo il risultato strutturato che l'azienda può usare per automatizzare il flusso
    print("Risultato dell'Agente (JSON):")
    print(risultato_json)
