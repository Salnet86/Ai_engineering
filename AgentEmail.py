import imaplib
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import google.generativeai as genai

# ==========================================
# CONFIGURAZIONE
# ==========================================
GEMINI_API_KEY = "LA_TUA_API_KEY_GEMINI"
EMAIL_USER = "tuamail@gmail.com"
EMAIL_PASS = "xxxx xxxx xxxx xxxx"  # App Password creata dal provider

# Server IMAP e SMTP (Esempio per Gmail)
IMAP_SERVER = "imap.gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Inizializzazione Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

class EmailAgent:
    def __init__(self, user, password, imap_server, smtp_server, smtp_port):
        self.user = user
        self.password = password
        self.imap_server = imap_server
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def read_unread_emails(self, limit=5):
        """Legge le ultime email non lette."""
        emails_data = []
        try:
            mail = imaplib.IMAP4_SSL(self.imap_server)
            mail.login(self.user, self.password)
            mail.select("inbox")

            # Cerca le mail non lette
            status, response = mail.search(None, 'UNSEEN')
            email_ids = response[0].split()

            # Prende le ultime 'limit' email
            for e_id in email_ids[-limit:]:
                status, data = mail.fetch(e_id, '(RFC822)')
                raw_email = data[0][1]
                msg = email.message_from_bytes(raw_email)

                # Estrazione corpo testo
                body = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                            break
                else:
                    body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')

                emails_data.append({
                    "id": e_id,
                    "from": msg.get("From"),
                    "subject": msg.get("Subject"),
                    "body": body.strip()
                })

            mail.logout()
        except Exception as e:
            print(f"Errore durante la lettura delle email: {e}")

        return emails_data

    def analyze_and_draft_response(self, email_info):
        """Usa Gemini per analizzare l'email e generare una risposta professionale."""
        prompt = f"""
Sei un assistente virtuale per la gestione della posta elettronica.
Analizza la seguente email ricevuta:

DA: {email_info['from']}
OGGETTO: {email_info['subject']}
TESTO:
{email_info['body']}

Compiti:
1. Valuta la priorità (Alta, Media, Bassa).
2. Determina l'intento principale in una frase.
3. Bozza una risposta formale e professionale in italiano (o nella lingua del mittente se diversa).

Formatta l'output esattamente così:
PRIORITÀ: [Valore]
INTENTO: [Valore]
RISPOSTA:
[Testo della risposta]
"""
        response = model.generate_content(prompt)
        return response.text

    def send_email(self, to_email, subject, body):
        """Invia una nuova email o risposta."""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.user
            msg['To'] = to_email
            msg['Subject'] = f"Re: {subject}" if not subject.startswith("Re:") else subject
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.user, self.password)
            server.sendmail(self.user, to_email, msg.as_string())
            server.quit()
            print(f"✅ Email inviata con successo a {to_email}")
        except Exception as e:
            print(f"❌ Errore durante l'invio dell'email: {e}")

# ==========================================
# ESECUZIONE AGENT
# ==========================================
if __name__ == "__main__":
    agent = EmailAgent(EMAIL_USER, EMAIL_PASS, IMAP_SERVER, SMTP_SERVER, SMTP_PORT)

    print("🔍 Controllo nuove email non lette...")
    unread_emails = agent.read_unread_emails(limit=3)

    if not unread_emails:
        print("Nessuna nuova email da elaborare.")
    else:
        for mail in unread_emails:
            print("\n--------------------------------------------------")
            print(f"📩 Nuova email da: {mail['from']}")
            print(f"📌 Oggetto: {mail['subject']}")

            # Analisi ed elaborazione con l'Agent
            analysis = agent.analyze_and_draft_response(mail)
            print("\n🤖 Analisi ed elaborazione Gemini:")
            print(analysis)

            # Opzionale: Invio automatico o previa conferma
            # agent.send_email(mail['from'], mail['subject'], "Testo bozza estratto...")
