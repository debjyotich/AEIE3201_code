int temp_pin=A0;
void setup(){
	Serial.begin(9600);
}
void loop(){
	int sensor_data = analogRead(temp_pin);
	float temp_mv = (sensor_data/1024.0)*5000;
	float temp_C = temp_mv/10;
	Serial.print("Temp in Degree C:");
	Serial.println(temp_C);
	delay(500);
}