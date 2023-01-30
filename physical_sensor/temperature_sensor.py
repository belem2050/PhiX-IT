import serial
import random


def simulateTemperature():
    return round(random.uniform(-20,40), 1)


def getTemperature():
    ser = serial.Serial('COM5')
    ser.flushInput()
    ser_bytes = ser.readline()
    decoded_value = float(ser_bytes[0:len(ser_bytes) - 2].decode("utf-8"))
    return decoded_value


if __name__ == '__main__':
    # temperature = getTemperature()
    '''works properly when arduino is temperature sensor is connected to arduino and instructions from : 
    https://itsourcecode.com/free-projects/arduino-projects/temperature-monitoring-system-using-arduino-and-python-live-data-plotting/
    are followed, otherwise it's just a simulation '''
    temperature = simulateTemperature()
    print(f"Local temperature = {temperature}")
