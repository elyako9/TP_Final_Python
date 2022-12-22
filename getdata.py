import json
import requests
import datetime  
import pandas as pd
import sqlite3

def actualizaracciones():
    api_key = "6_EaRTnvrjkOlmezcLQ2P6m7ldhHrzMg"
    ticker = input("ingrese el nombre de la Acción:")
    fechainicio = input("ingrese la fecha de inicio:")
    fechafin = input("ingrese la fecha de fin:")
    api_url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{fechainicio}/{fechafin}?adjusted=true&sort=asc&limit=120&apiKey={api_key}'
    r = requests.get(api_url)
    data = r.json()
    #return data


    #def copiaradb(data):
    dates = []
    for i in range(len(data['results'])):
        epoch_time = data['results'][i]['t']  
        the_datetime = str(datetime.datetime.fromtimestamp( epoch_time/1000 ))
        #print(the_datetime[:10])
        dates.append(the_datetime[:10])


    #resultados = datafija['results']
    df = pd.DataFrame(data['results'])
    columnas = ['Volumen','Peso del volumen','Precio apertura','Precio cierre','High','Low','Timestamp','N transacciones']
    df.columns=columnas
    df.insert(0, "Fecha", dates)
    #print(df)

    accion = data['ticker']
    try:
        con = sqlite3.connect("dbacciones")
        # Escribe los datos del nuevo DataFrame en una nueva tabla en SQLite
        df.to_sql(f"{accion}", con, if_exists="replace")
        con.close()
    except Exception as ex:
        print(ex)
        
    return None