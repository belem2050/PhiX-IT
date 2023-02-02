from sensors.SeismicSensor import SeismicSensor
from sensors.TemperatureSensor import TemperatureSensor
from sets.SetInterface import SetInterface


class VolcanicActivitySet(SetInterface):
    def __init__(self, name, city):
        super(VolcanicActivitySet, self).__init__(name, city)
        self.seismic_sensor = SeismicSensor(self.city, simulationMode=True)
        self.addSensor(self.seismic_sensor)
        self.temperature_sensor = TemperatureSensor(self.city)
        self.addSensor(self.temperature_sensor)

    def getVolcanicActivityRisk(self):
        seismic_activity = self.seismic_sensor.getSeismicActivity()
        volcanic_ground_temperature = self.temperature_sensor.getTemperature()

        if seismic_activity > 7 or (seismic_activity > 3 and volcanic_ground_temperature > 30):
            volcanic_activity_risk_message = "Major earthquake risk!"
        elif seismic_activity > 3 or volcanic_ground_temperature > 30:
            volcanic_activity_risk_message = "Minor earthquake risk!"
        else:
            volcanic_activity_risk_message = "No flooding risk."

        volcanic_activity_risk_dict = {
            'location': self.getLocation(),
            "message": volcanic_activity_risk_message,
            "seismic_activity": seismic_activity,
            "volcanic_ground_temperature": volcanic_ground_temperature
        }
        return volcanic_activity_risk_dict
