import datetime
import requests
from queue import Queue
from threading import Thread  
# import json 
 


# # ------------------------ Globale - Variablen --------------------------------
TOKEN = None
EXPIRYTIME = None
NUMBER_OF_CONSUMERS = 3
# -------------------------- Funktionen -----------------------------------------

def get_headers(): 
    global TOKEN, EXPIRYTIME
    if EXPIRYTIME is None or EXPIRYTIME <= datetime.datetime.now():
        print("Der Token ist abgelaufen")
        response = requests.post("example.com", data={"":""})
        data = response.json()
        TOKEN = data.get("access_token")
        EXPIRYTIME = datetime.datetime.now() + datetime.timedelta(seconds=890)
        print("Neuer Token wurde generiert")
        header = {
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/pdf",
        }
        return header
    else:
        expirationTime = EXPIRYTIME - datetime.datetime.now()
        print(f"Der Token ist noch gültig für: {expirationTime}")
        header = {
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/pdf",
        }
        return header

def producer(queue, items):
    print("producer: Daten werden generiert...")
    for item in items:
        queue.put(item)
    queue.put(None)
    print (f"producer: {queue.qsize()} Daten in der Queue")
    print(f"Anzahl der Consumer: {NUMBER_OF_CONSUMERS}")
    
    

# def get_token():
#     global TOKEN, expirytime
#     response = requests.post("example.com", data={"":""})
#     data = response.json()
#     TOKEN = data.get("access_token")
#     expirytime = datetime.datetime.now() + datetime.timedelta(seconds=890)
#     print("Neuer Token wurde generiert")
#     return TOKEN, expirytime

# def check_token():
#     global TOKEN, expirytime
#     if expirytime <= datetime.datetime.now():
#         print("Token ist abgelaufen")
#         TOKEN, expirytime = get_token()
#         return TOKEN, expirytime
#     else:
#         print("Token ist noch gültig")
#         return TOKEN, expirytime
    
    
    
# -------------------------- Funktionen - Ablauf -----------------------------------------
    

# get_token()
# get_registrationprotocols()
#  check_token()
# get_pdf_Name()
#  get_buisnesspremisesID()
    # check_token()
#  get_time()


 
# get_pdf()
#  check_token()
# send_pdf() v upload_pdf()