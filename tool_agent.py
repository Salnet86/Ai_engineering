from google import genai

client = genai.Client()

# 1. Definiamo una funzione Python che l'IA potrà usare come "strumento" (tool)
def calcola_consumo_energia(potenza_watt: float, ore_giornaliere: float) -> str:
    """Calcola il consumo energetico mensile in kWh di un dispositivo elettronico.
    
    Args:
        potenza_watt: La potenza del dispositivo in Watt.
        ore_giornaliere: Le ore di utilizzo medio al giorno.
    """
    kwh_giorno = (potenza_watt * ore_giornaliere) / 1000
    kwh_mese = kwh_giorno * 30
    return f"Il dispositivo consuma circa {kwh_mese:.2f} kWh al mese."

def avvia_agente_con_tool():
    print("=== AGENTE CON TOOL CALLING ===")
    
    domanda = "Ho un componente elettronico che consuma 150 Watt e rimane acceso 4 ore al giorno. Quanto consuma in un mese?"
    print(f"Domanda utente: {domanda}\n")
    
    # Chiediamo al modello di elaborare la richiesta usando la funzione Python come tool
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=domanda,
        config={
            # Passiamo la funzione direttamente nei tool dell'API
            "tools": [calcola_consumo_energia]
        }
    )
    
    # Se il modello decide di usare la funzione, l'SDK gestisce la chiamata
    print(f"Risposta dell'Agente:\n{response.text}")

if __name__ == "__main__":
    avvia_agente_con_tool()
  
