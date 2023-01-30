from API.openWeatherMapAPI import getTemperature


class AvalancheSet():
    def __init__(self):
        self.name = "avalanche set"

    def getAvalancheRisk(self, city):
        temperature = getTemperature(city)
        snow_depth = getSnowDepth(city)

        if snow_depth < 0.2:
            return "No avalanche risk"
        elif snow_depth > 0.5 and temperature > 0:
            return "Major avalanche risk"
        else:
            return "Minor avalanche risk"
