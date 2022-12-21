import requests

api_key = "6_EaRTnvrjkOlmezcLQ2P6m7ldhHrzMg"
api_url = f'https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2022-01-01/2022-01-10?adjusted=true&sort=asc&limit=120&apiKey={api_key}'
data = requests.get(api_url).json()
accion = data['ticker']
print(accion)

import datetime  
dates = []
for i in range(len(data['results'])):
  epoch_time = data['results'][i]['t']  
  the_datetime = str(datetime.datetime.fromtimestamp( epoch_time/1000 ))
  #print(the_datetime[:10])
  dates.append(the_datetime[:10])

import pandas as pd
#resultados = datafija['results']
df = pd.DataFrame(data['results'])
columnas = ['Volumen','Peso del volumen','Precio apertura','Precio cierre','High','Low','Timestamp','N transacciones']
df.columns=columnas
df.insert(0, "Fecha", dates)
print(df)

import sqlite3
con = sqlite3.connect("dbpython")
# Escribe los datos del nuevo DataFrame en una nueva tabla en SQLite
df.to_sql(f"{accion}", con, if_exists="replace")
#con.close()
###ver la opcion de hacer try: except

con = sqlite3.connect("dbpython")
cursor = con.cursor()
cursor.execute('SELECT name FROM sqlite_master WHERE type = "table";')
row = cursor.fetchall()
for g in range(len(row)):
  acc = row[g][0]
  cursor.execute(f'SELECT Fecha FROM {acc};')
  fechasacc = cursor.fetchall()
  print (f">>> {acc} - {fechasacc[0][0]} <--> {fechasacc[-1][0]}")
con.close()

