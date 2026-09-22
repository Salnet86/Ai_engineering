from google import genai

client = genai.Client()

# Simuliamo un database aziendale interno (es. un gestionale ERP)
database_aziendale = {
    "CL-1002": {"nome": "Mario Rossi", "stato_ordine": "Spedito", "tracking": "TRK-88392"},
    "CL-1045": {"nome": "Laura Bianchi", "stato_ordine": "In lavorazione", "tracking": "N/A"}
}

def cerca_nel_gestionale(codice_cliente: str) -> str:
    """Cerca i dati di spedizione del cliente nel database interno dell'azienda."""
    cliente = database_aziendale.get(codice_cliente)
    if cliente:
        return f"Cliente: {cliente['nome']}, Stato: {cliente['stato_ordine']}, Tracking: {cliente['tracking']}"
    return "Cliente non trovato nel database aziendale."

def gestisci_richiesta_enterprise(codice_cliente):
    # L'agente usa la funzione per recuperare i dati reali e riservati dal gestionale
    dati_cliente = cerca_nel_gestionale(codice_cliente)
    
    prompt = f"""
Agisci come l'assistente clienti ufficiale. Genera una risposta professionale per il cliente basandoti esclusivamente su questi dati aziendali interni:
{dati_cliente}
"""
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    print("=== INTERROGAZIONE SISTEMA ENTERPRISE ===")
    risposta = gestisci_richiesta_enterprise("CL-1002")
    print(risposta)
  
