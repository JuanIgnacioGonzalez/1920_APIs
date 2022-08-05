import requests
import json
import pandas as pd

url_dict = {
    '1': 'https://api.estadisticasbcra.com/usd_of', #dolarOficial
    '2': 'https://api.estadisticasbcra.com/usd',#dolarCcl   
    '3' : 'https://api.estadisticasbcra.com/leliq_usd',#leliqUsd
    '4' : 'https://api.estadisticasbcra.com/inflacion_mensual_oficial',#inflacionMensualOficial
    '5' : 'https://api.estadisticasbcra.com/base_usd',#baseUsd
    '6': 'https://api.estadisticasbcra.com/reservas_internacionales',#reservasInternacionales
    '7': 'https://api.estadisticasbcra.com/plazo_fijo',#plazoFijos
    '8': 'https://api.estadisticasbcra.com/cajas_ahorro',#cajaAhorro
    '9': 'https://api.estadisticasbcra.com/lebac',#lebacss
    '10': 'https://api.estadisticasbcra.com/usd_ccl_vs_oficial',#usdCclvsOficial
     
}

while True:
    D = input("Que decision quiere hacer: \n 1. Dolar Oficial \n 2. Dolar Ccl \n 3. LELIQ USD \n 4. Inflacion Mensual Oficial \n 5. Base USD \n 6. Reservas Internacionales \n 7. Plazo Fijo \n 8. Caja Ahorro \n 9. LELIQ USD \n 10. USD CCL vs Oficial \n 11. Salir \n")
    if D == '11':
        break
    try:
        
        Decision = url_dict[D]
        csvName = Decision.split('/')[-1]
        print(csvName)
        break
    except KeyError:
        print("No existe la decision")
        continue        




api_key = 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTEyNDAyNzQsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJ0b21hc2d1ZWxsMTIzQGdtYWlsLmNvbSJ9.hGOuRNd2s9ODdVAlSB94gAyG1UxFBlDboZiP_qvwnFJJCbLOPPlYVn2WEyiV9h2iitIuXk5Dl46HzM__8ucH5w'
api_header = 'BEARER eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTEyNDAyNzQsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJ0b21hc2d1ZWxsMTIzQGdtYWlsLmNvbSJ9.hGOuRNd2s9ODdVAlSB94gAyG1UxFBlDboZiP_qvwnFJJCbLOPPlYVn2WEyiV9h2iitIuXk5Dl46HzM__8ucH5w'

response = requests.get(Decision, headers={'Authorization': api_header}).text
#print(response)
json_response = json.loads(response)
#print(json_response)


pdObj = pd.DataFrame.from_records(json_response)
print(pdObj)
pdObj.to_csv(f'{csvName}.csv', index=True)
