import requests
import json


url_dict = {
    'dolarOficial': 'https://api.estadisticasbcra.com/usd_of',
    'leliqUsd' : 'https://api.estadisticasbcra.com/leliq_usd',
    'inflacionMensualOficial' : 'https://api.estadisticasbcra.com/inflacion_mensual_oficial',
    'dolarCcl': 'https://api.estadisticasbcra.com/usd'
    
    
    
}








url = 'https://api.estadisticasbcra.com/leliq_usd'

api_key = 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTEyNDAyNzQsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJ0b21hc2d1ZWxsMTIzQGdtYWlsLmNvbSJ9.hGOuRNd2s9ODdVAlSB94gAyG1UxFBlDboZiP_qvwnFJJCbLOPPlYVn2WEyiV9h2iitIuXk5Dl46HzM__8ucH5w'
api_header = 'BEARER eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTEyNDAyNzQsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJ0b21hc2d1ZWxsMTIzQGdtYWlsLmNvbSJ9.hGOuRNd2s9ODdVAlSB94gAyG1UxFBlDboZiP_qvwnFJJCbLOPPlYVn2WEyiV9h2iitIuXk5Dl46HzM__8ucH5w'

response = requests.get(url_dict['dolarCcl'], headers={'Authorization': api_header}).text
#print(response)
json_response = json.loads(response)
print(json_response)