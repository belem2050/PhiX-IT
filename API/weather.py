import requests # lit requête http
import json # encode et décode JSON

Location = input('post code of city : ')
Location = "fr."+Location
APP_KEY="779e6f7f895bea2f15eba6b89cfbb7f5"
APP_ID = "a6165965"
LocalWeatherType = "current"


x = requests.get(f'http://api.weatherunlocked.com/api/{LocalWeatherType}/{Location}?app_id={APP_ID}&app_key={APP_KEY}') # FAKE JSON file


print(x.text)

answer = json.loads(x.text)
print(answer["wx_desc"])
print(answer["wx_desc"])