from sensors.HumiditySensor import HumiditySensor
from sets.SetInterface import SetInterface


class FloodSet(SetInterface):
    def __init__(self, name, city):
        super(FloodSet, self).__init__(name, city)
        self.humidity_sensor = HumiditySensor(self.city)
        self.addSensor(self.humidity_sensor)

    def getFloodRisk(self):
        humidity = self.humidity_sensor.getHumidity()

        if humidity == 100:
            flood_risk_message = "Major flooding risk!"
        else:
            flood_risk_message = "No flooding risk."

        flood_risk_dict = {
            'location': self.getLocation(),
            "message": flood_risk_message,
            "humidity": humidity,
            # "humidity_history": self.humidity_sensor.getHumidityHistory()
        }
        return flood_risk_dict
