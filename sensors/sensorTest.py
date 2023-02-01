from sensors.ElevationSensor import ElevationSensor
from sensors.HumiditySensor import HumiditySensorInterface
from sensors.PhysicalTemperatureSensor import PhysicalTemperatureSensorInterface
from sensors.SnowfallSensor import SnowfallSensorInterface
from sensors.TemperatureSensor import TemperatureSensorInterface

if __name__ == "__main__":
    print("\n\n### testing local physical temperature sensor (in simulation mode) ###")
    local_temperature_sensor = PhysicalTemperatureSensorInterface()
    print(f"local_temperature_sensor.getName() : {local_temperature_sensor.getName()}")
    print(f"local_temperature_sensor.getSensorType() : {local_temperature_sensor.getSensorType()}")
    print(f"local_temperature_sensor.getCity() : {local_temperature_sensor.getCity()}")
    print(f"local_temperature_sensor.getExactCityName() : {local_temperature_sensor.getExactCityName()}")
    print(f"local_temperature_sensor.getLocation() : {local_temperature_sensor.getLocation()}")
    print(f"local_temperature_sensor.getLocalTemperature() : {local_temperature_sensor.getLocalTemperature()}")

    print("\n\n### testing temperature sensor for Mexico City ###")
    temperature_sensor = TemperatureSensorInterface("Mexico City")
    print(f"temperature_sensor.getName() : {temperature_sensor.getName()}")
    print(f"temperature_sensor.getSensorType() : {temperature_sensor.getSensorType()}")
    print(f"temperature_sensor.getCity() : {temperature_sensor.getCity()}")
    print(f"temperature_sensor.getExactCityName() : {temperature_sensor.getExactCityName()}")
    print(f"temperature_sensor.getLocation() : {temperature_sensor.getLocation()}")
    print(f"temperature_sensor.getTemperature() : {temperature_sensor.getTemperature()}")

    print("\n\n### testing humidity sensor for Lisbon ###")
    humidity_sensor = HumiditySensorInterface("Lisbon")
    print(f"humidity_sensor.getName() : {humidity_sensor.getName()}")
    print(f"humidity_sensor.getSensorType() : {humidity_sensor.getSensorType()}")
    print(f"humidity_sensor.getCity() : {humidity_sensor.getCity()}")
    print(f"humidity_sensor.getExactCityName() : {humidity_sensor.getExactCityName()}")
    print(f"humidity_sensor.getLocation() : {humidity_sensor.getLocation()}")
    print(f"humidity_sensor.getHumidity() : {humidity_sensor.getHumidity()}")

    print("\n\n### testing elevation sensor for Ax-les-Thermes ###")
    elevation_sensor = ElevationSensor("Ax-les-Thermes")
    print(f"elevation_sensor.getName() : {elevation_sensor.getName()}")
    print(f"elevation_sensor.getSensorType() : {elevation_sensor.getSensorType()}")
    print(f"elevation_sensor.getCity() : {elevation_sensor.getCity()}")
    print(f"elevation_sensor.getExactCityName() : {elevation_sensor.getExactCityName()}")
    print(f"elevation_sensor.getLocation() : {elevation_sensor.getLocation()}")
    print(f"elevation_sensor.getElevation() : {elevation_sensor.getElevation()}")

    print("\n\n### testing snowfall sensor for Rovaniemi ###")
    snowfall_sensor = SnowfallSensorInterface("Rovaniemi")
    print(f"snowfall_sensor.getName() : {snowfall_sensor.getName()}")
    print(f"snowfall_sensor.getSensorType() : {snowfall_sensor.getSensorType()}")
    print(f"snowfall_sensor.getCity() : {snowfall_sensor.getCity()}")
    print(f"snowfall_sensor.getExactCityName() : {snowfall_sensor.getExactCityName()}")
    print(f"snowfall_sensor.getLocation() : {snowfall_sensor.getLocation()}")
    print(f"snowfall_sensor.getSnowFall() : {snowfall_sensor.getSnowFall()}")
