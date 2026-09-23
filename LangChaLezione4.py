import os
import requests
from dataclasses import dataclass
from dotenv import load_dotenv


# Import di LangChain e LangGraph
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool, ToolRuntime
from langgraph.checkpoint.memory import MemorySaver


# 1. CARICAMENTO DELLE VARIABILI D'AMBIENTE
load_dotenv()
if not OPENAI_API_KEY := os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY non trovata nel file .env")




# ==========================================
# 2. DEFINIZIONE DEI DATACLASS (Contesto e Output Strutturato)
# ==========================================
@dataclass
class UserContext:
    user_id: str


@dataclass
class WeatherResponse:
    summary: str
    temperature_celsius: float
    humidity: str




# ==========================================
# 3. DEFINIZIONE DEGLI STRUMENTI (Tools)
# ==========================================
@tool
def get_weather(city: str) -> dict:
    """Restituisce le informazioni meteo in formato JSON per una data città."""
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    return response.json()


@tool
def locate_user(runtime: ToolRuntime[UserContext]) -> str:
    """Trova la città dell'utente in base al contesto (User ID)."""
    user_id = runtime.context.user_id
    # Simulazione di un database utente
    if user_id == "ABC123":
        return "Vienna"
    elif user_id == "XYZ456":
        return "London"
    return "Roma"




# ==========================================
# 4. CONFIGURAZIONE DELL'AGENTE AVANZATO
# ==========================================
# Inizializzazione del modello linguistico
llm_model = init_chat_model("gpt-4o-mini", temperature=0.3)


# Memoria della conversazione basata su Thread ID
memory_checkpointer = MemorySaver()


# Creazione dell'agente completo
weather_agent = create_agent(
    model=llm_model,
    tools=[get_weather, locate_user],
    system_prompt="Sei un assistente meteo simpatico, utile e preciso.",
    context_schema=UserContext,
    response_format=WeatherResponse,
    checkpointer=memory_checkpointer
)




# ==========================================
# 5. ESECUZIONE E TEST DELL'AGENTE
# ==========================================
if __name__ == "__main__":
    # Configurazione della sessione (Thread ID per la memoria)
    session_config = {"configurable": {"thread_id": "sessione_utente_1"}}


    # Iniezione del contesto utente (es. user_id = "ABC123" corrisponde a Vienna)
    current_context = UserContext(user_id="ABC123")


    print("Invio della richiesta all'agente...")
    result = weather_agent.invoke(
        {"messages": [{"role": "user", "content": "Che tempo fa oggi?"}]},
        config=session_config,
        context=current_context
    )


    # Stampa dell'output strutturato definito in WeatherResponse
    print("\nRisultato strutturato ottenuto:")
    print(result["structured_response"])

