import requests
import json

def sendPost(entrada, salida):

    url = "http://192.168.100.218:4000/vision"
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    data = {
        "entrada": entrada,
        "salida": salida
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.status_code

# PRueba de cliente post con json
# respuesta = sendPost("entrada", "salida", "total")
# print(respuesta)

def sendPostTotal(total):

    url = "http://192.168.100.218:4000/total"
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    data = {
        "total": total
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.status_code