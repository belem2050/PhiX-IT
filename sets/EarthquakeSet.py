from sensors.SeismicSensor import SeismicSensor
from sets.SetInterface import SetInterface


class EarthquakeSet(SetInterface):
    def __init__(self, name, city):
        super(EarthquakeSet, self).__init__(name, city)
        self.seismic_sensor = SeismicSensor(self.city, simulationMode=True)
        self.addSensor(self.seismic_sensor)

    def getEarthquakeRisk(self):
        seismic_activity = self.seismic_sensor.getSeismicActivity()

        if seismic_activity > 7:
            earthquake_risk_message = "Major earthquake risk!"
        elif seismic_activity > 3:
            earthquake_risk_message = "Minor earthquake risk!"
        else:
            earthquake_risk_message = "No earthquake risk."

        earthquake_risk_dict = {
            'location': self.getLocation(),
            "message": earthquake_risk_message,
            "seismic_activity": seismic_activity,
        }
        return earthquake_risk_dict
