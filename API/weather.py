import requests
import json

API_key = "2f2111a9e20f5023a246278a428cd9dc"


x = requests.request(f'api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99&appid={API_key}')

print(x.text)

answer = json.loads(x.text)

print(x.text)