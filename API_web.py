import os
import hug
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

#Pasarela para entrar en la API
scope = ['https://spreadsheets.google.com/feeds']

#Credenciales. Usamos variables de entorno para no colgar información sensible en github
mydictcreds ={"type": os.environ["TYPE"],
"project_id": os.environ["PROJECT_ID"],
"private_key_id": os.environ["PRIVATE_KEY_ID"],
"private_key":os.environ['PRIVATE_KEY'],
"client_email": os.environ["CLIENT_EMAIL"],
"client_id": os.environ["CLIENT_ID"],
"auth_uri": os.environ["AUTH_URI"],
"token_uri": os.environ["TOKEN_URI"],
"auth_provider_x509_cert_url": os.environ["AUTH_PROVIDER_X509"],
"client_x509_cert_url": os.environ["CLIENT_X509"]
}

creds = ServiceAccountCredentials.from_json_keyfile_dict(mydictcreds, scope)    #Nos conectamos
client = gspread.authorize(creds)



#creds = ServiceAccountCredentials.from_json_keyfile_name('BotCS-0877f1f9375e.json', scope)
                                              #Nos autorizamos

@hug.get('/')
def raiz():
    return{ "status":"OK" }

@hug.get('/victorias')
def victorias():
    sheet = client.open('CS:GO Database WeRkAh/Graná').sheet1
    result = sheet.cell(4,17).value
    return { "victorias":result }
