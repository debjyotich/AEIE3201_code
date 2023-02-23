#include "DHT.h"
#define DHTPIN 2
#define DHT_TYPE DHT11
DHT dht(DHTPIN,DHT_TYPE);
void setup(){
	Serial.begin(9600);
	dht.begin();
}
void loop(){
	float t= dht.readTemperature();
	float h= dht.readHumidity();
	Serial.print("Temp: ");
	Serial.println(t);
	Serial.print("Hum: ");
	Serial.println(h);
	delay(500);
}