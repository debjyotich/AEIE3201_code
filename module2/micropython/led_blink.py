from machine import pin
from utime import sleep
d_5=Pin(14,Pin.OUT)


while True:
    d_5.on()
    sleep(1)
    d_5.off()
    sleep(1)
           