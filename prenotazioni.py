import gspread

from google.oauth2.service_account import Credentials
import os

# Definisce lo scope
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# here we set as environmental variables in Railway these credentials so as to be kept secret

creds_dict = {
    "type": os.environ.get('GOOGLE_TYPE'),
    "project_id": os.environ.get('GOOGLE_PROJECT_ID'),
    "private_key_id": os.environ.get('GOOGLE_PRIVATE_KEY_ID'),
    "private_key": os.environ.get('GOOGLE_PRIVATE_KEY').replace('\\n', '\n'),
    "client_email": os.environ.get('GOOGLE_CLIENT_EMAIL'),
    "client_id": os.environ.get('GOOGLE_CLIENT_ID'),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
}
creds = Credentials.from_service_account_info(creds_dict, scopes=scope)

# Autorizza il client con le credenziali
client = gspread.authorize(creds)

# Apri il foglio di calcolo tramite il suo ID che abbiamo settato con environment variable in Railway
GOOGLE_SHEET_ID = os.environ.get('GOOGLE_SHEET_ID')
sheet = client.open_by_key(GOOGLE_SHEET_ID).sheet1

# Funzione di inserimento
def inserisci_ticket(nome_completo, telefono, email, tipo_cliente, motivo, urgenza, data):
    print(f"Nome: {nome_completo} Telefono: {telefono} Email: {email} Tipo di cliente: {tipo_cliente} Motivo: {motivo} Urgenza: {urgenza} Data: {data}")
    
    # Inserisci la riga nello sheet
    row_to_insert = [nome_completo, telefono, email, tipo_cliente, motivo, urgenza,data]
    sheet.append_row(row_to_insert)
    

