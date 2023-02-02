import random
from sensors.SensorInterface import SensorInterface


class PrecipitationSensor(SensorInterface):
    def __init__(self, city, name="precipitation sensor", sensor_type="virtual", simulationMode=False):
        super(PrecipitationSensor, self).__init__(city, name, sensor_type)
        self.simulationCounter = 0

    def getPrecipitation(self):
        if not self.simulationMode:
            pass
        else:
            # we are going to prioritize no precipitation for the simulation, the rain only occurs sometimes
            if self.simulationCounter == 5:
                self.simulationCounter = 0
                return round(random.uniform(0.2, 30), 1)
            else:
                return 0

    def getPrecipitationHistory(self):
        pass

