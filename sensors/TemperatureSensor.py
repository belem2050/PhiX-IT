from API.openWeatherMapAPI import getWeatherInfo
from SensorInterface import Sensor


class TemperatureSensor(Sensor):
    def __init__(self, city, name="temperature sensor", sensor_type="virtual"):
        super(TemperatureSensor, self).__init__(city, name, sensor_type)

    def getTemperature(self):
        return getWeatherInfo(self.city)['ActualWeather']['temperature']
