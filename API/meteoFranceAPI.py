import requests
import json

from API.locationUtils import convertCityToLocation, getExactCityName

API_key = "c59628809c75f22f1e9002b0173f3c9b"


def getData(location):
    x = requests.get(
        f'https://api.open-meteo.com/v1/meteofrance?latitude={location[0]}&longitude={location[1]}&hourly=snowfall&daily=snowfall_sum&current_weather=true&timezone=auto', verify=False)
    json_data = json.loads(x.text)
    return json_data


if __name__ == "__main__":
    city = "Helsinki"
    location = convertCityToLocation(city)
    print(location)
    print(location[0], location[1])
    print(f"city : {city}\ndetected location = {getExactCityName(city)}\tlatitude = {location[0]}, longitude = {location[1]}")
    print(getData(location)['current_weather'].keys())
    print(getData(location)['hourly'].keys())

