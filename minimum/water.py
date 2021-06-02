import gpiozero
import w1thermsensor
import Adafruit_DHT
import time
import math


distance = gpiozero.DistanceSensor(trigger = 16, echo = 10)
motor = gpiozero.Buzzer(3)
therm = w1thermsensor.W1ThermSensor()
humid = Adafruit_DHT.DHT22

distance.distance * 100

motor.beep(on_time=time, off_time=0, n=1)
print("motor on")

therm.get_temperature()

Adafruit_DHT.read_entry(Adafruit_DHT.DHT22, 4)[9]
       