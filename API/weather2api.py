import requests # lit requête http
import json # encode et décode JSON

Location = input('post code of the city : ')
Location = "fr."+Location
APP_KEY="9d0804bd0ac1549985268ca3b72730a0"
APP_ID = "a6165965"
LocalWeatherType = "current"


x = requests.get(f'http://api.weatherunlocked.com/api/{LocalWeatherType}/{Location}?app_id={APP_ID}&app_key={APP_KEY}') # 


print(x.text)

answer = json.loads(x.text)

