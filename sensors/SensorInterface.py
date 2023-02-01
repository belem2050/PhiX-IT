from API.locationUtils import convertCityToLocation, getExactCityName


class SensorInterface:

    def __init__(self, city, name, sensor_type):
        self.name = name
        self.sensor_type = sensor_type
        self.city = city
        self.exact_city = getExactCityName(city)
        self.location = convertCityToLocation(self.exact_city)

    def getName(self):
        return self.name

    def getSensorType(self):
        return self.sensor_type

    def getCity(self):
        return self.city

    def getExactCityName(self):
        return self.exact_city

    def getLocation(self):
        return self.location


