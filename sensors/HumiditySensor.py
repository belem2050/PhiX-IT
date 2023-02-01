from API.openWeatherMapAPI import getWeatherInfo
from sensors.SensorInterface import SensorInterface


class HumiditySensorInterface(SensorInterface):
    def __init__(self, city, name="humidity sensor", sensor_type="virtual"):
        super(HumiditySensorInterface, self).__init__(city, name, sensor_type)

    def getHumidity(self):
        return getWeatherInfo(self.city)['ActualWeather']['humidity']


