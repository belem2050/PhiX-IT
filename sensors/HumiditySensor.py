from API.openWeatherMapAPI import getWeatherInfo
from SensorInterface import Sensor


class HumiditySensor(Sensor):
    def __init__(self, city, name="humidity sensor", sensor_type="virtual"):
        super(HumiditySensor, self).__init__(city, name, sensor_type)

    def getHumidity(self):
        return getWeatherInfo(self.city)['ActualWeather']['humidity']


