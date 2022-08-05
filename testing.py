import requests
import json
import pandas as pd



"""
https://api.estadisticasbcra.com/milestones : eventos relevantes (presidencia, ministros de economía, presidentes del BCRA, cepo al dólar)
https://api.estadisticasbcra.com/base : base monetaria
https://api.estadisticasbcra.com/base_usd: base monetaria dividida USD
https://api.estadisticasbcra.com/base_usd_of: base monetaria dividida USD Oficial
https://api.estadisticasbcra.com/reservas : reservas internacionales
https://api.estadisticasbcra.com/base_div_res : base monetaria dividida reservas internacionales
https://api.estadisticasbcra.com/usd : cotización del USD
https://api.estadisticasbcra.com/usd_of : cotización del USD Oficial
https://api.estadisticasbcra.com/usd_of_minorista : cotización del USD Oficial (Minorista)
https://api.estadisticasbcra.com/var_usd_vs_usd_of : porcentaje de variación entre la cotización del USD y el USD oficial
https://api.estadisticasbcra.com/circulacion_monetaria : circulación monetaria
https://api.estadisticasbcra.com/billetes_y_monedas : billetes y monedas
https://api.estadisticasbcra.com/efectivo_en_ent_fin : efectivo en entidades financieras
https://api.estadisticasbcra.com/depositos_cuenta_ent_fin : depositos de entidades financieras en cuenta del BCRA
https://api.estadisticasbcra.com/depositos : depósitos
https://api.estadisticasbcra.com/cuentas_corrientes : cuentas corrientes
https://api.estadisticasbcra.com/cajas_ahorro : cajas de ahorro
https://api.estadisticasbcra.com/plazo_fijo : plazos fijos
https://api.estadisticasbcra.com/tasa_depositos_30_dias : tasa de interés por depósitos
/////
https://api.estadisticasbcra.com/prestamos : prestamos
https://api.estadisticasbcra.com/tasa_prestamos_personales : tasa préstamos personales
https://api.estadisticasbcra.com/tasa_adelantos_cuenta_corriente : tasa adelantos cuenta corriente
https://api.estadisticasbcra.com/porc_prestamos_vs_depositos : porcentaje de prestamos en relación a depósitos
https://api.estadisticasbcra.com/lebac : LEBACs
https://api.estadisticasbcra.com/leliq : LELIQs
https://api.estadisticasbcra.com/lebac_usd : LEBACs en USD
https://api.estadisticasbcra.com/leliq_usd : LELIQs en USD
https://api.estadisticasbcra.com/leliq_usd_of : LELIQs en USD Oficial
https://api.estadisticasbcra.com/tasa_leliq : Tasa de LELIQs
https://api.estadisticasbcra.com/m2_privado_variacion_mensual : M2 privado variación mensual
https://api.estadisticasbcra.com/cer : CER
https://api.estadisticasbcra.com/uva : UVA
https://api.estadisticasbcra.com/uvi : UVI
https://api.estadisticasbcra.com/tasa_badlar : tasa BADLAR
https://api.estadisticasbcra.com/tasa_baibar : tasa BAIBAR
https://api.estadisticasbcra.com/tasa_tm20 : tasa TM20
https://api.estadisticasbcra.com/tasa_pase_activas_1_dia : tasa pase activas a 1 día
https://api.estadisticasbcra.com/tasa_pase_pasivas_1_dia : tasa pase pasivas a 1 día
https://api.estadisticasbcra.com/inflacion_mensual_oficial : inflación mensual oficial
https://api.estadisticasbcra.com/inflacion_interanual_oficial : inflación inteanual oficial
https://api.estadisticasbcra.com/inflacion_esperada_oficial : inflación esperada oficial
https://api.estadisticasbcra.com/dif_inflacion_esperada_vs_interanual : diferencia entre inflación interanual oficial y esperada
https://api.estadisticasbcra.com/var_base_monetaria_interanual : variación base monetaria interanual
https://api.estadisticasbcra.com/var_usd_interanual : variación USD interanual
https://api.estadisticasbcra.com/var_usd_oficial_interanual : variación USD (Oficial) interanual
https://api.estadisticasbcra.com/var_merval_interanual : variación merval interanual
https://api.estadisticasbcra.com/var_usd_anual : variación anual del dólar (porcentaje de variación de la cotización del dólar un año despues a la cotización de la fecha indicada)
https://api.estadisticasbcra.com/var_usd_of_anual : variación anual del dólar oficial (porcentaje de variación de la cotización del dólar oficial un año despues a la cotización de la fecha indicada)
https://api.estadisticasbcra.com/var_merval_anual : variación anual del MERVAL (porcentaje de variación del MERVAL un año despues al la cotización de la fecha indicada)
https://api.estadisticasbcra.com/merval : MERVAL
https://api.estadisticasbcra.com/merval_usd : MERVAL dividido cotización del USD

"""

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



url = 'https://api.estadisticasbcra.com/leliq_usd'

api_key = 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTEyNDAyNzQsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJ0b21hc2d1ZWxsMTIzQGdtYWlsLmNvbSJ9.hGOuRNd2s9ODdVAlSB94gAyG1UxFBlDboZiP_qvwnFJJCbLOPPlYVn2WEyiV9h2iitIuXk5Dl46HzM__8ucH5w'
api_header = 'BEARER eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTEyNDAyNzQsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJ0b21hc2d1ZWxsMTIzQGdtYWlsLmNvbSJ9.hGOuRNd2s9ODdVAlSB94gAyG1UxFBlDboZiP_qvwnFJJCbLOPPlYVn2WEyiV9h2iitIuXk5Dl46HzM__8ucH5w'

response = requests.get(Decision, headers={'Authorization': api_header}).text
#print(response)
json_response = json.loads(response)
#print(json_response)


pdObj = pd.DataFrame.from_records(json_response)
print(pdObj)
pdObj.to_csv(f'{csvName}.csv', index=True)
