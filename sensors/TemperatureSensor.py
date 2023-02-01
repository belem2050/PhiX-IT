from API.openWeatherMapAPI import getWeatherInfo
from sensors.SensorInterface import SensorInterface


class TemperatureSensorInterface(SensorInterface):
    def __init__(self, city, name="temperature sensor", sensor_type="virtual"):
        super(TemperatureSensorInterface, self).__init__(city, name, sensor_type)

    def getTemperature(self):
        return getWeatherInfo(self.city)['ActualWeather']['temperature']
