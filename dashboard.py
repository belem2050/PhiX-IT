import requests # read requête http
import json # encode and decode JSON
from flask import Flask, render_template, jsonify # to create our own API
from flask import Flask, render_template #for the dashboard
from datetime import datetime

from sets.AvalancheSet import AvalancheSet
from sets.FloodSet import FloodSet

#This program create an API localhost that make itself a request of another API: OpenWeatherMap

API_key="daf82e45c51760dfd726beb50392e1d7"
app = Flask(__name__)


# Create our own API since localhost

# Access from a siteweb : http://localhost:5000/api/flood/
@app.route('/api/flood/')
def avalanche():
    city_name = "Bordeaux"
    flood_set = FloodSet("avalanche set Bordeaux", city_name)

    flood_risk_dict = flood_set.getFloodRisk()
    # print(flood_risk_dict)
    return jsonify(flood_risk_dict)

# Access from a siteweb : http://localhost:5000/api/avalanche/
@app.route('/api/avalanche/')
def avalanche():
    city_name = "Ax-les-Thermes"
    avalanche_set = AvalancheSet("avalanche set Ax-les-Thermes", city_name)

    avalanche_risk_dict = avalanche_set.getAvalancheRisk()
    # print(avalanche_risk_dict)
    return jsonify(avalanche_risk_dict)


# Access from a siteweb : http://localhost:5000/api/forecaster/
@app.route('/api/forecaster/')
def forecaster():
    city_name = 'Toulouse'

    x = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_key}') 
    
    current = json.loads(x.text)
    
    #print(current)
    #print(current.keys())
    
    #weather = current["weather"][0] 
    #print(weather)
    
    main = current["main"]
    
    temperature = (main['temp'])
    pressure = main['pressure']
    humidity = main['humidity']
    
    
    #print(f'TEMPERATURE : {temperature}')
    #print(f'PRESSURE : {pressure}')
    #print(f'HUMIDITY : {humidity}')
    
    
    #Get the predictions weather of last 5 days
    y = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=metric&appid={API_key}') 
    
    
    predictions5days = json.loads(y.text)
    
    temperatureAverage = 0
    pressureAverage = 0
    humidityAverage = 0
    
    #get the predictions only 1 day (take the 8 first values)
    predictions1day = predictions5days['list'][0:8]
    
    for i in range(8):
        temperatureAverage += predictions1day[i]['main']['temp']
        pressureAverage += predictions1day[i]["main"]['pressure']
        humidityAverage += predictions1day[i]["main"]['humidity']
    
    temperatureAverage = temperatureAverage/8
    pressureAverage = pressureAverage/8
    humidityAverage = humidityAverage/8
    
    dictionnaire = {
        'type': 'Forecaster',
        'ActualWeather': {'temperature': temperature,
                          'pressure': pressure,
                          'humidiy': humidity},
        'TomorrowWeather': {'temperature': temperatureAverage,
                            'pressure': pressureAverage,
                            'humidiy': humidityAverage},
        'unitsTemp': "degrés Celcius"
    }
    return jsonify(dictionnaire)

#Access from a siteweb : http://localhost:5000/api/weather/
@app.route('/api/weather/')
def weather():

    city_name = 'Toulouse'

    response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=metric&appid={API_key}') 
    content = json.loads(response.content.decode('utf-8'))

    main = content["list"]

    dateList = []
    tempList = []
    for i in range(len(main)):
        timestamp = main[i]["dt"]
        date = datetime.fromtimestamp(timestamp)
        temp = main[i]['main']['temp']
        dateList.append(date)
        tempList.append(temp)
    
    date_temp = {'date': dateList,
                 'temp': tempList}

    return date_temp

# URL : http://localhost:5000/dashboard/
@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)

    