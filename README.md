# Modulo: Tecniche e Tecnologie per l'AI (30 Ore) corso python web app 
**AI Engineering e Integrazione Pratica dei Modelli Linguistici (LLM)**

Questo percorso raccoglie le istruzioni di configurazione e i codici sorgente sviluppati per il modulo formativo.

---

## ⚙️ 1. Configurazione dell'Ambiente e Installazione Librerie

pip install google-genai openai streamlit chromadb pillow



# Windows (CMD):
set GEMINI_API_KEY="tua-chiave-api-di-google"
# Mac / Linux:
export GEMINI_API_KEY="tua-chiave-api-di-google"


🧠 2. Concetti Teorici Chiave dell'AI Engineering
A differenza della Data Science (che si concentra sull'addestramento dei modelli matematici), l'AI Engineering si concentra sull'ingegneria del software applicata all'IA:
Cos'è un LLM e come si usa: I modelli non "pensano" come gli umani, ma prevedono la parola successiva basandosi su enormi quantità di dati. L'ingegnere li governa attraverso prompt strutturati e configurazioni di sistema.
Gestione della Memoria e delle Chat: Per creare un assistente fluido, il software deve mantenere la cronologia della conversazione (chat.chats.create), inviando lo storico a ogni nuova richiesta affinché il modello ricordi i messaggi precedenti.
Sistemi RAG (Retrieval-Augmented Generation): Per evitare che l'IA inventi risposte (allucinazioni), si utilizza un'architettura in cui i documenti aziendali interni vengono cercati e dati in pasto al modello come "contesto" prima che risponda.
Function Calling (Agenti IA): Permette all'intelligenza artificiale di decidere autonomamente quando eseguire una funzione scritta in Python (es. calcoli matematici, interrogazione di un database) per risolvere un problema complesso.
🏢 3. Applicazioni nel Mondo Aziendale (Enterprise AI)
Nel modulo sono stati esaminati i principali casi d'uso richiesti dal mercato del lavoro moderno:
Smistamento Automatico delle Email:
Come funziona: L'IA legge i messaggi in arrivo dal customer service, li analizza e restituisce un file JSON strutturato (categoria, urgenza, azione_consigliata) pronto per essere letto da altri software aziendali.
Motori di Ricerca Aziendali (Stile Perplexity):
Come funziona: Unione di ricerca web in tempo reale e RAG per trovare informazioni aggiornate e citare automaticamente le fonti originarie.
Integrazione Enterprise (ERP / CRM):
Come funziona: Sistemi multi-agente sicuri che si collegano ai database interni dell'azienda (es. magazzino, ordini, fatturazione) tramite connettori protetti e rigorose barriere di privacy, evitando che i dati sensibili escano dai server aziendali.

Come impostare la chiave di Google Gemini (GEMINI_API_KEY)

Su Windows (Prompt dei comandi - CMD):

set GEMINI_API_KEY="la_tua_chiave_gemini"
Su Windows (PowerShell):

$env:GEMINI_API_KEY="la_tua_chiave_gemini"
Su Mac / Linux (Terminal):

export GEMINI_API_KEY="la_tua_chiave_gemini


Come impostare la chiave di OpenAI (OPENAI_API_KEY)


Su Windows (Prompt dei comandi - CMD):

set OPENAI_API_KEY="la_tua_chiave_openai"



Su Windows (PowerShell):

$env:OPENAI_API_KEY="la_tua_chiave_openai"


Su Mac / Linux (Terminal):

export OPENAI_API_KEY="la_tua_chiave_openai"

💡 Nota importante:
I comandi scritti nel terminale valgono solo per quella specifica sessione. Se chiudi il terminale, dovrai impostarli di nuovo (oppure puoi aggiungerli permanentemente nelle Variabili d'ambiente del pannello di controllo di Windows o nel file di configurazione della shell su Mac/Linux come .bashrc o .zshrc).
Quando scrivi il comando, sostituisci "la_tua_chiave_..." con la stringa della chiave che hai generato dal rispettivo portale sviluppatori, lasciando però le virgolette.

note teoriche 
L'AI Engineering è la disciplina che unisce l'ingegneria del software tradizionale all'intelligenza artificiale generativa, con un obiettivo chiaro: portare l'IA fuori dal browser e trasformarla in applicazioni reali, stabili e produttive per le aziende.
A differenza della Data Science (che si concentra sulla matematica, la ricerca scientifica e l'addestramento dei modelli da zero), l'AI Engineer non crea il "motore", ma sa come assemblarlo, collegarlo ai sistemi informatici e farlo funzionare in modo efficiente.
I Pilastri dell'AI Engineering
Il lavoro di un AI Engineer si basa su quattro competenze fondamentali:
Integrazione tramite API: Saper utilizzare i modelli esistenti (come Google Gemini o OpenAI) attraverso linguaggi di programmazione come Python, gestendo le richieste, le risposte e la memoria delle conversazioni.
Architetture RAG (Retrieval-Augmented Generation): Poiché i modelli non conoscono i segreti di un'azienda, l'ingegnere crea sistemi che leggono i documenti interni, li indicizzano in database vettoriali e li forniscono all'IA come "contesto" per evitare che inventi risposte (allucinazioni).
Agenti e Function Calling: Non solo chat, ma automazione. L'AI Engineer programma l'intelligenza artificiale affinché sappia quando chiamare funzioni esterne (es. calcoli matematici, invio di email, interrogazione di un database gestionale).
Produzione e Sicurezza (LLMOps): Ottimizzare i costi delle chiamate API, garantire la privacy dei dati aziendali (spesso utilizzando modelli open-source in locale) e inserire barriere di sicurezza per evitare errori o comportamenti anomali.
In sintesi, l'AI Engineer è il professionista che trasforma l'intelligenza artificiale da semplice "curiosità tecnologica" a uno strumento aziendale concreto, sicuro e integrato.





1. **Crea e attiva un ambiente virtuale:**
   ```bash
   python -m venv venv
   # Windows (CMD):
   venv\Scripts\activate
   # Mac / Linux:
   source venv/bin/activate
