# Installazione della libreria (se necessario):
# pip install langchain openai


from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


# Configurazione della chiave API e del modello
# (Assicurati di impostare la variabile d'ambiente OPENAI_API_KEY)
llm = OpenAI(temperature=0.7)


# Creazione di un Prompt Template
prompt = PromptTemplate(
    input_variables=["product"],
    template="Qual è un buon nome per un'azienda che produce {product}?",
)


# Creazione della Chain che unisce il prompt e il modello
chain = LLMChain(llm=llm, prompt=prompt)


# Esecuzione della chain passando l'input
result = chain.run(product="scarpe da corsa ecologiche")
print(result)

