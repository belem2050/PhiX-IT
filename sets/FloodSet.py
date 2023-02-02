from sensors.PrecipitationSensor import PrecipitationSensor
from sensors.WaterLevelSensor import WaterLevelSensor
from sets.SetInterface import SetInterface


class FloodSet(SetInterface):
    def __init__(self, name, city):
        super(FloodSet, self).__init__(name, city)
        self.precipitation_sensor = PrecipitationSensor(self.city, simulationMode=True)
        self.addSensor(self.precipitation_sensor)
        self.water_level_sensor = WaterLevelSensor(self.city, simulationMode=True)
        self.addSensor(self.water_level_sensor)

    def getFloodRisk(self):
        water_level = self.water_level_sensor.getWaterLevel()
        precipitation = self.precipitation_sensor.getPrecipitation()

        if water_level == "critical" or (water_level == "high" and precipitation > 10):
            flood_risk_message = "Major flooding risk!"
        elif water_level == "high":
            flood_risk_message = "Minor flooding risk!"
        else:
            flood_risk_message = "No flooding risk."

        flood_risk_dict = {
            'location': self.getLocation(),
            "message": flood_risk_message,
            "water_level": water_level,
            "precipitation": precipitation
        }
        return flood_risk_dict
