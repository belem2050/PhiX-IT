from API.openWeatherMapAPI import getWeatherInfo
from sensors.SensorInterface import SensorInterface


class HumiditySensor(SensorInterface):
    def __init__(self, city, name="humidity sensor", sensor_type="virtual"):
        super(HumiditySensor, self).__init__(city, name, sensor_type)

    def getHumidity(self):
        return getWeatherInfo(self.city)['ActualWeather']['humidity']

    def getHumidityHistory(self):
        return getWeatherInfo(self.city)['HumidityHistory']


