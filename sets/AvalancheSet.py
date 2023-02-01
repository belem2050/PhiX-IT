from sensors.ElevationSensor import ElevationSensor
from sensors.SnowfallSensor import SnowfallSensor
from sensors.PhysicalTemperatureSensor import PhysicalTemperatureSensor
from sets.SetInterface import SetInterface


class AvalancheSet(SetInterface):
    def __init__(self, name, city):
        super(AvalancheSet, self).__init__(name, city)
        self.local_temperature_sensor = PhysicalTemperatureSensor(self.city, simulationMode=True)
        self.addSensor(self.temperature_sensor)
        self.elevation_sensor = ElevationSensor(self.city)
        self.addSensor(self.elevation_sensor)
        self.snowfall_sensor = SnowfallSensor(self.city)
        self.addSensor(self.snowfall_sensor)

    def getAvalancheRisk(self):
        temperature = self.local_temperature_sensor.getLocalTemperature()
        elevation = self.elevation_sensor.getElevation()
        snow_fall = self.snowfall_sensor.getSnowFall()

        if elevation < 500 or snow_fall == 0:
            avalanche_risk_message = "No avalanche risk"
        elif elevation > 1200 and snow_fall > 2 and temperature > 0:
            avalanche_risk_message = "Major avalanche risk"
        else:
            avalanche_risk_message = "Minor avalanche risk"

        snow_history = self.snowfall_sensor.getSnowHistory()

        avalanche_risk_dict = {
            "location": self.getLocation(),
            "message": avalanche_risk_message,
            "temperature": temperature,
            "elevation": elevation,
            "snow_fall": snow_fall,
            "snow_history": snow_history,
        }
        return avalanche_risk_dict
