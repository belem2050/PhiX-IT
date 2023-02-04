import requests # lit requête http
import json # encode et décode JSON

Location = input('post code of city : ')
Location = "fr."+Location
APP_KEY="9d0804bd0ac1549985268ca3b72730a0"
APP_ID = "a6165965"
LocalWeatherType = "current"
resort_id = "999001"
#api.weatherunlocked.com/api/resortforecast/999001?app_id={APP_ID}&app_key={APP_KEY}


x = requests.get(f'http://api.weatherunlocked.com/api/{LocalWeatherType}/{Location}?app_id={APP_ID}&app_key={APP_KEY}') # 

#y = requests.get(f'api/resortforecast/{resort_id}?app_id={APP_ID}&app_key={APP_KEY}') # 
z = requests.get('http://api.weatherapi.com/v1/forecast.json?key=ecd0158fe1724980b2e221850233001&q=paris&days=1&aqi=no&alerts=no')
w = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key=ecd0158fe1724980b2e221850233001&q=07112&days=7')


print(w.text)
#print(y.text)

answer = json.loads(x.text)
#print(answer)3140

