from machine import Pin
import dht,utime
from ConsentiumThings import ThingsUpdate

api_key=""
ssid= ""
psk=""

board= ThingsUpdate(key=api_key)
board.initWiFi(ssid,psk)
d=dht.DHT11(Pin(14))

while True:
    d.measure()
    sensor_val=[d.temperature(),d.humidity()]
    print(sensor_val)
    info_buff=["Temperature","Humidity"]
    r=board.sendREST(info_buff,sensor_val)
    print(r)
    utime.sleep(5)