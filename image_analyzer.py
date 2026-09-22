from google import genai
from PIL import Image

client = genai.Client()

def analizza_immagine(percorso_immagine, prompt):
    print(caricamento f"Caricamento dell'immagine: {percorso_immagine}...")
    try:
        # Carica l'immagine usando la libreria standard Pillow (PIL)
        img = Image.open(percorso_immagine)
        
        print("Invio dell'immagine e del prompt al modello...")
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            # Passiamo sia l'oggetto immagine che il testo nella lista dei contents
            contents=[img, prompt]
        )
        return response.text
    except Exception as e:
        return f"Errore durante l'elaborazione dell'immagine: {e}"

if __name__ == "__main__":
    # Sostituisci con il percorso di una tua immagine di prova (es. un PNG o JPG)
    percorso = "schema_prova.jpg"
    domanda = "Descrivi cosa vedi in questa immagine e spiega i dettagli principali."
    
    # Nota: Assicurati di avere un'immagine nella stessa cartella o metti il percorso corretto
    print(f"=== ANALIZZATORE MULTIMODALE ===")
    print(f"Prompt: {domanda}\n")
    
    # Esempio di esecuzione (assicurati che il file esista per testarlo)
    # risposta = analizza_immagine(percorso, domanda)
    # print(f"\nRisposta:\n{risposta}")
    print("Salva uno schema o un'immagine nella cartella, decommenta le righe nel blocco principale e prova lo script!")
