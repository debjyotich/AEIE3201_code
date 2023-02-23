int relay_pin=12;
int ldr_pin=A0;
#define THRES 780
void setup(){
	Serial.begin(9600);
	pinMode(relay_pin,OUTPUT);
}
void loop(){
	int light_inten=analogRead(ldr_pin);
	if(light_inten>=THRES){
		digitalWrite(relay_pin,HIGH);
		Serial.println('Light ON!");
	}
	else{
		digitalWrite(relay_pin,LOW);
	Serial.println('Light OFF");
	}	
	delay(100);
}