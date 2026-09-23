import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import BaseOutputParser


# 1. Caricamento delle variabili d'ambiente
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


if not api_key:
    raise ValueError("OPENAI_API_KEY non trovata. Controlla il file .env")


# Inizializzazione del modello
chat_model = ChatOpenAI(openai_api_key=api_key)




# ==========================================
# 2. ESEMPIO BASE: Chiamata Semplice
# ==========================================
print("--- 1. Esempio Base ---")
result_base = chat_model.predict("Hello, how can I assist you today?")
print(result_base)
print()




# ==========================================
# 3. MESSAGGI MULTIPLI (Contesto e Regole)
# ==========================================
print("--- 2. Messaggi Multipli ---")
messages = [
    HumanMessage(content="From now on 1 + 1 = 3. Use this in your replies."),
    HumanMessage(content="What is 1 + 1?"),
    HumanMessage(content="What is 1 + 1 + 1?")
]
result_messages = chat_model.predict_messages(messages)
print(result_messages.content)
print()




# ==========================================
# 4. PROMPT TEMPLATE
# ==========================================
print("--- 3. Prompt Template ---")
template = "You are a helpful assistant that translates {input_language} to {output_language}."
human_template = "{text}"


chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template)
])


formatted_messages = chat_prompt.format_messages(
    input_language="English",
    output_language="French",
    text="I love programming"
)
result_prompt = chat_model.predict_messages(formatted_messages)
print(result_prompt.content)
print()




# ==========================================
# 5. CHAIN CON OPERATORE PIPE (|) E PARSER
# ==========================================
print("--- 4. Chain e Output Parser ---")


class CommaSeparatedListOutputParser(BaseOutputParser):
    def parse(self, text: str):
        return text.strip().split(", ")


list_template = "You are a helpful assistant who generates comma separated list. A user will pass in a category and you should generate 5 objects in that category. Only return a comma separated list and nothing more."
list_human_template = "{text}"


list_chat_prompt = ChatPromptTemplate.from_messages([
    ("system", list_template),
    ("human", list_human_template)
])


# Unione di prompt, modello e parser tramite la pipe (|)
chain = list_chat_prompt | chat_model | CommaSeparatedListOutputParser()


result_chain = chain.invoke({"text": "colors"})
print(result_chain)

