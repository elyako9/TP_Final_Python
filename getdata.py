import json
import requests

def pedirdatos():
    api_key = "6_EaRTnvrjkOlmezcLQ2P6m7ldhHrzMg"
    ticker = input("ingrese el nombre de la Acción:")
    fechainicio = input("ingrese la fecha de inicio:")
    fechafin = input("ingrese la fecha de fin:")
    api_url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{fechainicio}/{fechafin}?adjusted=true&sort=asc&limit=120&apiKey={api_key}'
    r = requests.get(api_url)
    data = r.json()
    return data