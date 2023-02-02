import random
from sensors.SensorInterface import SensorInterface


class WaterLevelSensor(SensorInterface):
    def __init__(self, city, name="water level sensor", sensor_type="virtual", simulationMode=False):
        super(WaterLevelSensor, self).__init__(city, name, sensor_type)
        self.simulationMode = simulationMode
        self.simulationCounter = 0

    def getWaterLevel(self):
        if not self.simulationMode:
            pass
        else:
            random_case = random.randint(0, 5)
            if random_case == 0:
                return "low"
            elif random_case == 1 or random_case == 2:  # we are prioritizing "mediun" water level
                return "medium"
            elif random_case == 3:
                return "high"
            else:
                return "critical"

    def getWaterLevelHistory(self):
        pass

