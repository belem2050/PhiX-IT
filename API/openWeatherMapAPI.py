import requests
import json
from datetime import datetime


API_key = "c59628809c75f22f1e9002b0173f3c9b"


def getWeatherInfo(city_name="Toulouse"):

    x = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_key}', verify=False)
    json_data = json.loads(x.text)
    data = json_data["main"]

    temperature = data['temp']
    pressure = data['pressure']
    humidity = data['humidity']

    # Get the predictions weather of last 5 days
    y = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=metric&appid={API_key}', verify=False)

    predictions5days = json.loads(y.text)

    main = predictions5days["list"]

    temperatureAverage = 0
    pressureAverage = 0
    humidityAverage = 0

    humidityList = []
    dateList = []
    for i in range(len(main)):
        humidity = main[i]['main']['humidity']
        humidityList.append(humidity)

        timestamp = main[i]["dt"]
        date = datetime.fromtimestamp(timestamp)
        dateList.append(date)

    # get the predictions only 1 day (take the 8 first values)
    predictions1day = predictions5days['list'][0:8]

    for i in range(8):
        temperatureAverage += predictions1day[i]['main']['temp']
        pressureAverage += predictions1day[i]["main"]['pressure']
        humidityAverage += predictions1day[i]["main"]['humidity']

    temperatureAverage = temperatureAverage / 8
    pressureAverage = pressureAverage / 8
    humidityAverage = humidityAverage / 8

    weatherInfo = {
        'type': 'Forecaster',
        'ActualWeather': {'temperature': temperature,
                          'pressure': pressure,
                          'humidity': humidity},
        'TomorrowWeather': {'temperature': temperatureAverage,
                            'pressure': pressureAverage,
                            'humidity': humidityAverage},
        'HumidityHistory': humidityList,
        'dateHistory' : dateList,
        'unitsTemp': "degrés Celcius"
    }
    return weatherInfo


if __name__ == "__main__":
    city = "Toulouse"
    weatherDetails = getWeatherInfo(city)
    print(f"Weather for {city} : \n{weatherDetails}")
