# import gpiozero
# import w1thermsensor
# import Adafruit_DHT
import time
import math

class Ultrasonic:
    TRIG = 16
    ECHO = 10
    # sensor = gpiozero.DistanceSensor(trigger = TRIG, echo = ECHO)

    def get_water_level(self):
        return math.random() * 100
        # return self.sensor.distance * 100

class Motor:
    PIN = 3
    # motor = gpiozero.Buzzer(PIN)

    def water(self, time):
        # self.motor.beep(on_time=time, off_time=0, n=1)
        print("motor on")

class Thermometer:
    # PIN = 5
    # sensor = w1thermsensor.W1ThermSensor()

    def get_temperature(self):
        # return self.sensor.get_temperature()
        return math.random() * 30


class Hygrometer:
    # PIN = 4
    # SENSOR = Adafruit_DHT.DHT22

    def get_humidity(self):
        # return Adafruit_DHT.read_entry(self.SENSOR, self.PIN)[9]
        return math.random() * 100

def mainloop():
    while 1:
        # Just starting it off at 10hz for now
        time.sleep(0.1)
        print("bruh")
