from API.locationUtils import convertCityToLocation


class SetInterface:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.location = convertCityToLocation(city)
        self.sensor_list = []
        self.number_of_sensors = 0

    def addSensor(self, sensor):
        self.sensor_list.append(sensor)
        self.number_of_sensors += 1

    def deleteSensor(self, sensor_name):
        for sensor in self.sensor_list:
            if sensor.getName() == sensor_name:
                self.sensor_list.remove(sensor)
                self.number_of_sensors -= 1

    def deleteSensor(self, sensor):
        for s in self.sensor_list:
            if s.equals(sensor):
                self.sensor_list.remove(sensor)
                self.number_of_sensors -= 1

    def getName(self):
        return self.name

    def getLocation(self):
        return self.location

    def getSensorList(self):
        return self.sensor_list

    def getNumberOfSensors(self):
        return self.number_of_sensors
