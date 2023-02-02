import random
from sensors.SensorInterface import SensorInterface


class SeismicSensor(SensorInterface):
    def __init__(self, city, name="seismic sensor", sensor_type="virtual", simulationMode=False):
        super(SeismicSensor, self).__init__(city, name, sensor_type)
        self.simulationCounter = 0

    def getSeismicActivity(self):
        if not self.simulationMode:
            pass
        else:
            # we are going to prioritize no seismic activity for the simulation as not often earthquakes occur
            # or volcanoes erupt
            if self.simulationCounter == 5:
                self.simulationCounter = 0
                return round(random.uniform(0.5, 10), 1)
            else:
                return 0

    def getSeismicActivityHistory(self):
        pass

