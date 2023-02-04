from API.meteoFranceAPI import getData
from sensors.SensorInterface import SensorInterface


class ElevationSensor(SensorInterface):
    def __init__(self, city, name="elevation sensor", sensor_type="virtual"):
        super(ElevationSensor, self).__init__(city, name, sensor_type)

    def getElevation(self):
        return getData(self.location)['elevation']


