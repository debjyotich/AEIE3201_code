#include <ConsentiumThings.h>
#include "DHT.h"

#define DHTPIN 2
#define DHT_TYPE DHT11

ConsentiumThings board;   // create ConsentiumThing object
DHT dht(DHTPIN,DHT_TYPE);

const char *ssid = ""; // add WiFi SSID
const char *pass = ""; // add WiFi password
const long interval = 5; // take 5 seconds of delay 
const char *key = "";       // Write api key

void setup(){
  board.begin();   // init. IoT boad
  dht.begin();
  board.initWiFi(ssid, pass);  // begin WiFi connection
}

void loop(){
	float t= dht.readTemperature();
	float h= dht.readHumidity();

    float sensor_val[] = {t, h};  // sensor data array
    String info_buff[] = {"Temperature", "Humidity"}; // sensor info. array
  
    int sensor_num = sizeof(sensor_val)/sizeof(sensor_val[0]); // number of sensors connected 
  
    board.sendREST(key, sensor_num, info_buff, sensor_val, LOW_PRE, interval); // send over REST with delay with desired prescision
}