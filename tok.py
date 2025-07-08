import datetime
import requests
# import json

# ----------------------------- Globale - Variablen --------------------------------------
username = "example_user"
password = "example_password"
# ----------------------------- Klassen --------------------------------------------------

class Tokenmanager:
    global username, password
    
    def __init__(self, url, headers, payload):
        self.url = url
        self.headers = headers
        self.payload = payload
        self.token = None
        self.expirytime = datetime.datetime.now()
        self.status = None
 
    def get_token(self):
        response = requests.post(self.url, data=self.payload)
        data = response.json()
        self.token = data.get("access_token")
        self.expirytime = datetime.datetime.now() + datetime.timedelta(seconds=890)
        self.status = response.raise_for_status()
        print("Neuer Token wurde generiert")
        return self.token

    def test_token(self):
        if self.expirytime <= datetime.datetime.now():
            print("Token ist abgelaufen")
            self.token = self.get_token()
            return self.token
        else:
            print("Token ist noch gültig")


# -------------------------- Main Fluss -----------------------------------------
manager = Tokenmanager(url="example.com", headers={"":""}, payload={"username": username, "password": password})
print(manager.get_token())

# -------------------------------------------------------------------------------
# -------------------------- ohne Klassen ---------------------------------------


# # ------------------------ Globale - Variablen --------------------------------
# token = None
# expirytime = None
# -------------------------- Funktionen -----------------------------------------

# def get_token():
#     global token, expirytime
#     response = requests.post("example.com", data={"":""})
#     data = response.json()
#     token = data.get("access_token")
#     expirytime = datetime.datetime.now() + datetime.timedelta(seconds=890)
#     print("Neuer Token wurde generiert")
#     return token, expirytime

# def check_token():
#     global token, expirytime
#     if expirytime <= datetime.datetime.now():
#         print("Token ist abgelaufen")
#         token, expirytime = get_token()
#         return token, expirytime
#     else:
#         print("Token ist noch gültig")
#         return token, expirytime
    
