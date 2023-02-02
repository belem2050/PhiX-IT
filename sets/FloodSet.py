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
        humidity = self.humidity_sensor.getHumidity()

        if humidity > 95:
            flood_risk_message = "Major flooding risk!"
        elif humidity > 80:
            flood_risk_message = "Minor flooding risk!"
        else:
            flood_risk_message = "No flooding risk."

        flood_risk_dict = {
            'location': self.getLocation(),
            "message": flood_risk_message,
            "humidity": humidity,
            # "humidity_history": self.humidity_sensor.getHumidityHistory()
        }
        return flood_risk_dict
