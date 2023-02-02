import requests
import json
from geopy.geocoders import Nominatim

API_key = "c59628809c75f22f1e9002b0173f3c9b"


def getData(city_name):
    location = convertCitytoGeo(city_name)
    x = requests.get(
        f'https://api.open-meteo.com/v1/meteofrance?latitude={location.latitude}&longitude={location.longitude}&hourly=snowfall&daily=snowfall_sum&current_weather=true&timezone=auto')
    json_data = json.loads(x.text)
    return json_data

def getSnowFall(city_name):
    sumSnowFall = 0
    for snow in getData(city_name)['hourly']['snowfall']:
        if snow is not None:
            sumSnowFall += snow
    return round(sumSnowFall, 2)

def getElevation(city_name):
    return getData(city_name)['elevation']

def convertCitytoGeo(city_name):
    geolocator = Nominatim(user_agent="MyApp")  # Initialize Nominatim API
    location = geolocator.geocode(city_name)  # get location
    # print("The latitude of the location is: ", location.latitude)
    # print("The longitude of the location is: ", location.longitude)
    return location


if __name__ == "__main__":
    city = "Helsinki"
    print(f"city : {city}\ndetected location = {convertCitytoGeo(city)}\tlatitude = {convertCitytoGeo(city).latitude}, longitude = {convertCitytoGeo(city).latitude}")
    print(f"elevation = {getElevation(city)}")
    print(f"recent snowfall = {getSnowFall(city)}")

