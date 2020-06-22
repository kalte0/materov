// Arduino file vvv
// ~/clubRPI/basicSerialIno.ino

#include <Wire.h>
#include <ArduinoJson.h>
#include <Adafruit_LEDBackpack.h>
#include <Adafruit_GFX.h>

Adafruit_7segment matrix = Adafruit_7segment(); 

char hotgos;
int     size_ = 0;
String  payload;

void setup() {
	Serial.begin(9600);
	pinMode(LED_BUILTIN, OUTPUT);
	digitalWrite(LED_BUILTIN, HIGH);
	delay(1000);
	digitalWrite(LED_BUILTIN, LOW);
	delay(1000);
	matrix.begin(0x70); // Code for the 7seg - write a quick test. 
	matrix.print(100);
	matrix.writeDisplay(); 
	
}

void loop() {
//	serialReadNumber();
	serialReadJson();
}


int serialReadNumber() { // old method only here for basic serial troubleshooting
	if (Serial.available()) { //when get Serial info:
		int inChar = Serial.read(); 
		hotgos = (char)inChar;
		if (hotgos == (char)'4') {
			digitalWrite(LED_BUILTIN, HIGH);	
		}
		else { 
			digitalWrite(LED_BUILTIN, LOW);
		}
	}
}

int serialReadJson() {
	if (Serial.available()) { 
		Serial.println("Serial Available");
		while ( !Serial.available()) {}
		payload = Serial.readStringUntil('/n');	
	}
	StaticJsonDocument<512> doc; //This creates a temporary JsonDocument called doc. 

	DeserializationError error = deserializeJson(doc, payload); // error detection
	if (error) {
		matrix.print(1010);
		Serial.println(error.c_str());
		matrix.writeDisplay(); 
	}

	else{
		if (doc["axis0"] <= 10) { // If it can read the "test" value from the document:
			//Serial.println("You succeeded");
			int y = doc["axis0"]; // done because not sure if matrix.print can read from an array.  
			Serial.print(y); 
			matrix.print(y);
			matrix.writeDisplay(); 
		}
		else {
			matrix.print(1111); //Failure message
			matrix.writeDisplay(); 
		}
	}
	
}

