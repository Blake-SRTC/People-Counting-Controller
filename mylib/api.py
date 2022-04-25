import requests
import json

def sendPost(entrada, salida, total):

    url = "http://192.168.100.218:4000/vision"
    # data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    data = {
        "Entrada": entrada,
        "Salida": salida,
        "Total": total
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.status_code

# PRueba de cliente post con json
# respuesta = sendPost("entrada", "salida", "total")
# print(respuesta)