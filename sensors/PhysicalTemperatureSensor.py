import serial
import random
from SensorInterface import Sensor


class PhysicalTemperatureSensor(Sensor):
    def __init__(self, city="Toulouse", name="local temperature sensor", sensor_type="physical",
                 simulationMode=True):
        super(PhysicalTemperatureSensor, self).__init__(city, name, sensor_type)
        self.simulationMode = simulationMode

    def getLocalTemperature(self):
        if self.simulationMode:
            return round(random.uniform(-20, 40), 1)
        else:
            ser = serial.Serial('COM5')
            ser.flushInput()
            ser_bytes = ser.readline()
            decoded_value = float(ser_bytes[0:len(ser_bytes) - 2].decode("utf-8"))
            return decoded_value
