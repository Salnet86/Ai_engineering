from openai import OpenAI
import json

client = OpenAI()

# 1. Definiamo la funzione Python classica
def calcola_consumo_energia(potenza_watt: float, ore_giornaliere: float) -> str:
    """Calcola il consumo energetico mensile in kWh di un dispositivo elettronico."""
    kwh_giorno = (potenza_watt * ore_giornaliere) / 1000
    kwh_mese = kwh_giorno * 30
    return f"Il dispositivo consuma circa {kwh_mese:.2f} kWh al mese."

# 2. Creiamo la specifica dello strumento (tool) da passare a OpenAI
tools_config = [
    {
        "type": "function",
        "function": {
            "name": "calcola_consumo_energia",
            "description": "Calcola il consumo energetico mensile in kWh di un dispositivo elettronico.",
            "parameters": {
                "type": "object",
                "properties": {
                    "potenza_watt": {
                        "type": "number",
                        "description": "La potenza del dispositivo in Watt."
                    },
                    "ore_giornaliere": {
                        "type": "number",
                        "description": "Le ore di utilizzo medio al giorno."
                    }
                },
                "required": ["potenza_watt", "ore_giornaliere"]
            }
        }
    }
]

def esegui_agente_openai():
    domanda = "Ho un apparecchio che consuma 200 Watt e sta acceso 5 ore al giorno. Quanto consuma in un mese?"
    print(f"Domanda utente: {domanda}\n")
    
    messages = [{"role": "user", "content": domanda}]
    
    # Prima chiamata: il modello analizza la richiesta e decide se chiamare la funzione
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools_config,
        tool_choice="auto"
    )
    
    response_message = response.choices[0].message
    
    # Controlliamo se il modello ha deciso di invocare una funzione
    if response_message.tool_calls:
        print("L'IA ha deciso di utilizzare lo strumento (Function Calling)...\n")
        
        # Estraiamo i dettagli della chiamata
        tool_call = response_message.tool_calls[0]
        func_name = tool_call.function.name
        func_args = json.loads(tool_call.function.arguments)
        
        # Eseguiamo la funzione Python localmente sul computer
        if func_name == "calcola_consumo_energia":
            risultato_funzione = calcola_consumo_energia(
                potenza_watt=func_args["potenza_watt"],
                ore_giornaliere=func_args["ore_giornaliere"]
            )
            
            print(f"Risultato calcolato dalla funzione locale: {risultato_funzione}")
            
            # Aggiungiamo la risposta della funzione alla cronologia per rimandarla al modello
            messages.append(response_message)
            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": func_name,
                "content": risultato_funzione
            })
            
            # Seconda chiamata: inviamo il risultato al modello affinché formuli la risposta finale per l'utente
            final_response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )
            
            print(f"\nRisposta finale dell'Agente:\n{final_response.choices[0].message.content}")

if __name__ == "__main__":
    esegui_agente_openai()
  
