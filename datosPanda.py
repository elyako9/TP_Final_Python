import requests

api_key = "6_EaRTnvrjkOlmezcLQ2P6m7ldhHrzMg"
api_url = f'https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2022-01-01/2022-01-10?adjusted=true&sort=asc&limit=120&apiKey={api_key}'
data = requests.get(api_url).json()
#print(data)

import datetime  
dates = []
for i in range(len(data['results'])):
  epoch_time = data['results'][i]['t']  
  the_datetime = str(datetime.datetime.fromtimestamp( epoch_time/1000 ))
  #print(the_datetime[:10])
  dates.append(the_datetime[:10])

import pandas as pd
#resultados = datafija['results']
df = pd.DataFrame(data['results'], index=dates)
columnas = ['Volumen','Peso del volumen','Precio apertura','Precio cierre','High','Low','Timestamp','N transacciones']
df.columns=columnas
print(df)