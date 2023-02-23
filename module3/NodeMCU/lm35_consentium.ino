#include <ConsentiumThings.h>

ConsentiumThings board;   // create ConsentiumThing object
int temp_pin=A0;
const char *ssid = ""; // add WiFi SSID
const char *pass = ""; // add WiFi password
const long interval = 5; // take 5 seconds of delay 
const char *key = "";       // Write api key

void setup(){
  board.begin();   // init. IoT boad
  board.initWiFi(ssid, pass);  // begin WiFi connection
}

void loop(){
	int sensor_data = analogRead(temp_pin);
	float temp_mv = (sensor_data/1024.0)*5000;
	float temp_C = temp_mv/10;
    float sensor_val[] = {temp_C};  // sensor data array
    String info_buff[] = {"Temperature"}; // sensor info. array
  
    int sensor_num = sizeof(sensor_val)/sizeof(sensor_val[0]); // number of sensors connected 
  
    board.sendREST(key, sensor_num, info_buff, sensor_val, LOW_PRE, interval); // send over REST with delay with desired prescision
}