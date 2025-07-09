import datetime
import requests
from queue import Queue
from threading import Thread  
# import json 
 


# # ------------------------ Globale - Variablen --------------------------------
TOKEN = None
EXPIRYTIME = None
UPLOAD_TYPE = "Mail"
# -------------------------- Funktionen -----------------------------------------

def get_headers(): 
    global TOKEN, EXPIRYTIME
    if EXPIRYTIME is None or EXPIRYTIME <= datetime.datetime.now():
        print("Der Token ist abgelaufen")
        response = requests.post("https://fiskal.cloud/auth/realms/df/protocol/openid-connect/token", headers = {"Accept": "application/pdf","Content-Type": "application/x-www-form-urlencoded"} , 
                                 data={"client_id": "df-api","grant_type": "password","username": "example","password": "password"})
        print(response)
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



def get_registrationprotocols():
    response = requests.get("https://fiskal.cloud/api/eric/registration-protocols", headers=get_headers())
    print(response)
    data = response.json()
    result = data.get("results")
    return result



def get_pdf_name(businesspremiseID):
    response = requests.get(f"https://fiskal.cloud/api/management/business-premises/{businesspremiseID}", headers=get_headers())
    data = response.json()
    businessPremisesIdentifier = data.get("businessPremisesIdentifier")
    time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return businessPremisesIdentifier + "_" + time + ".pdf"



def producer(queue, items):
    print("producer: Daten werden generiert...")
    for item in items:
        queue_item = {
            "fileName" : get_pdf_name(item.get("businessPremisesId")),
            "registrationprotocolID" : item.get("id"),
            "UploadType" : UPLOAD_TYPE
        }
        queue.put(queue_item)
    queue.put(None)
    print (f"producer: {queue.qsize()} Daten in der Queue")


#-------------------------- Main - Ablauf ---------------------------------------

items = get_registrationprotocols()


  
queue = Queue()
producer_thread = Thread(target=producer, args=(queue, items))
producer_thread.start()

# Warten bis alle Threads durch sind
producer_thread.join()
print(queue.qsize())





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