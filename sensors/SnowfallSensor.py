from API.meteoFranceAPI import getData
from SensorInterface import Sensor


class SnowfallSensor(Sensor):
    def __init__(self, city, name="snowfall sensor", sensor_type="virtual"):
        super(SnowfallSensor, self).__init__(city, name, sensor_type)

    def getSnowFall(self):
        sum_snow_fall = 0
        for snow in getData(self.location)['hourly']['snowfall']:
            if snow is not None:
                sum_snow_fall += snow
        return round(sum_snow_fall, 2)


