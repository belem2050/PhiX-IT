
import requests
import json

 

def getPrecipitation():
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"

    querystring = {"lat":"35.5","lon":"-78.5"}

    headers = {
        "X-RapidAPI-Key": "27283b1ab5msh3362f92a605b7a6p12f459jsn164769904591",
        "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    json_data = json.loads(response.text)

    #precipitation = json_data[""]
    return (json_data["data"][0])



def precipi():

    API_key= "c0389a227547a10206fda87a10455d77"
    x = requests.get(f'https://maps.openweathermap.org/maps/2.0/radar/forecast/6/13/24?&appid={API_key}&tm=1600781400')

    print(x.text)
    json_data = json.loads(x.text)
    

#print(getPrecipitation())
precipi()




