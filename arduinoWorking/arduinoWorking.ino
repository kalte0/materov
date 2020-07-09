
#include <Wire.h>
#include <ArduinoJson.h>
#include <Adafruit_LEDBackpack.h>
#include <Adafruit_GFX.h>

Adafruit_7segment matrix = Adafruit_7segment();
char hotgos;


void setup() {
  Serial.begin(9600);
  matrix.begin(0x70);
  matrix.print(0000);
  matrix.writeDisplay(); // write 100 just to make the screen is working. 
}

void loop() {
  if (Serial) { // if the serial communication is open:
    matrix.print(1000); // numbering system: generally, each 1 is one "step", from left to right. 1st step, connecting through serial, is complete. 
    matrix.writeDisplay(); 
  }
  if (Serial.available()) { // If there is a number waiting to be read through serial. 
    hotgos = Serial.read(); // information comes in as bytes.  
    if (hotgos == '2') { // If we can read what is being sent (the number two), success message or failure. 
      matrix.print(1100); 
      matrix.writeDisplay();
    }
  }
  
  Serial.println("Can you hear me?");
    
 
  delay(500); 
}


// Note to self: "" is a string, 'A' char,
//'A' = 65
