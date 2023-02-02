from sensors.HumiditySensor import HumiditySensor
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
        self.humidity_sensor = HumiditySensor(self.city, simulationMode=True)
        self.addSensor(self.humidity_sensor)

    def getFloodRisk(self):
        water_level = self.water_level_sensor.getWaterLevel()
        precipitation = self.precipitation_sensor.getPrecipitation()
        humidity = self.humidity_sensor.getHumidity()

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
            "precipitation": precipitation,
            "humidity": humidity,
            "humidity_history": self.humidity_sensor.getHumidityHistory()
        }
        return flood_risk_dict
