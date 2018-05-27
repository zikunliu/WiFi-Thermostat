from w1thermsensor import W1ThermSensor
def get_temp_from_sensor():
        sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "041703ee74ff")
        temperature_in_celsius = sensor.get_temperature()
        temp=int(32+temperature_in_celsius*1.8)
        return temp