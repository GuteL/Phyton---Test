import datetime
import requests


dt = datetime.datetime.now()
bt = dt + datetime.timedelta(seconds=900)
token = None

# -------------------------------------------------------------------------

def get_token():
    global token
    
    url = "example.com"
    
    heahders = {
        "":""
    }
    
    payload = {
         "":""
     }
    
    response = requests.post(url, data=payload, headers=headers)
    data = response.json()
    token = data.get("access_token")
    return token


def test():
    global bt, token
    dt_now = datetime.datetime.now()
    if dt_now >= bt:
        token = get_token()
        print("neuer Token")
        bt = dt_now + datetime.timedelta(seconds=900)
    else:
        print("Token ist noch gültig")


# -------------------------------------------------------------------------------


test()
print(bt)
