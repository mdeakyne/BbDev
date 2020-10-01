from os import getenv as ge
from dotenv import load_dotenv
from requests_toolbelt import sessions
from msal import ConfidentialClientApplication

load_dotenv()

def team_client():
    client_id = ge('client_id')
    authority_id = ge('authority_id')
    client_credential = ge('client_credential')

    BASE_URL = "https://graph.microsoft.com/beta/"
    ms_s = sessions.BaseUrlSession(base_url=BASE_URL)

    app = ConfidentialClientApplication(client_id=client_id,
                                        authority=f"https://login.microsoftonline.com/{authority_id}",
                                        client_credential=client_credential)

    result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
    token = result['access_token']
    sessions.BaseUrlSession(base_url='https://graph.microsoft.com/beta/')

    ms_s.headers.update({"Authorization":f"Bearer {token}"})
    return ms_s

def bb_client():
    