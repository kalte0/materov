
#include <Wire.h>
#include <ArduinoJson.h>
#include <Adafruit_LEDBackpack.h>
#include <Adafruit_GFX.h>

Adafruit_7segment matrix = Adafruit_7segment();
char hotgos;
String payload; 


void setup() {
  Serial.begin(9600);
  matrix.begin(0x70);
  matrix.print(0000);
  matrix.writeDisplay(); // write 100 just to make the screen is working. 
  Serial.println("Can you hear me?"); // Test to make sure that Serial read working.
  // Note: Writing conventions for this project: "<" At beginning for all serial messages. 
}

void loop() {
  
  if (Serial.available()) {
    //Serial.println("Serial Available");
    while ( ! Serial.available()) {
      matrix.print(404);
      matrix.writeDisplay(); 
      delay(50); 
      }
    payload = Serial.readStringUntil('/n');
  }
  StaticJsonDocument<512> doc; // Creates a temporary JsonDocument called "doc"
  DeserializationError error = deserializeJson(doc, payload); // error detection:
  if (error) {
    Serial.print("whoopsie encountered: ");
    Serial.println(error.c_str());
    matrix.print(999); 
    matrix.writeDisplay(); 
  }

  else {
    Serial.print("doc[test] reads: "); 
    char what = doc["test"];
    Serial.println(what); // way to condense this with printf?
    matrix.print(222); 
    matrix.writeDisplay(); 
  }

  //Serial.println("Still alive"); 
  delay(500); 
}


// Note to self: "" is a string, 'A' char,
//'A' = 65

/* Temporary place for easy access to the old serial code: 
 if (Serial.available()) { // If there is a number waiting to be read through serial. 
    hotgos = Serial.read(); // information comes in as bytes.  
    if (hotgos == '2') { // If we can read what is being sent (the number two), success message or failure. 
      matrix.print(1100); 
      matrix.writeDisplay();
    }
  }
 */
