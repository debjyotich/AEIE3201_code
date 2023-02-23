{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh15140\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 int temp_pin=A1;\
void setup() \{\
	Serial.begin(9600);\
\}\
void loop() \{\
	int sensor_data = analogRead(temp_pin);\
	float temp_mv = (sensor_data/1024.0)*5000;\
	float temp_C = temp_mv/10;\
	Serial.print("Temp in Degree C:");\
	Serial.println(temp_C);\
	delay(500);\
\}}