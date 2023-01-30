from API.openWeatherMapAPI import getTemperature, getHumidity


class AvalancheSet():
    def __init__(self):
        self.name = "avalanche set"

    def getAvalancheRisk(self, city):
        temperature = getTemperature(city)
        humidity = getHumidity(city)
        # we use humidity cuz no snow depth information are easily available from APIs
        
        if temperature < -15 and humidity < 20:
            return "No avalanche risk"
        elif temperature > 0 and humidity > 80:
            return "Major avalanche risk"
        else:
            return "Minor avalanche risk"

        ''' # ideally we would use snow depth for avalanche prediction ...
        snow_depth = getSnowDepth(city)

        if snow_depth < 0.2:
            return "No avalanche risk"
        elif snow_depth > 0.5 and temperature > 0:
            return "Major avalanche risk"
        else:
            return "Minor avalanche risk"'''
