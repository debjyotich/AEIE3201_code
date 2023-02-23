from machine import Pin
from utime import sleep
import dht

d=dht.DHT11(Pin(14))


while True:
    d.measure()
    print("Temp : ",d.temperature())
    print("Humidity : ",d.humidity())
    sleep(5)       