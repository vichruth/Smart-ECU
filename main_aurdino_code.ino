#include "model.h"
const int SENSOR_PIN = 34; 

Eloquent::ML::Port::RandomForestClassifier classifier;

void setup() {
  Serial.begin(115200);
  pinMode(SENSOR_PIN, INPUT);
  
  Serial.println("Smart ECU Initialized...");
  delay(2000);
}

void loop() {
  float rpm = analogRead(SENSOR_PIN);
  float features[] = { rpm };
  int prediction = classifier.predict(features);
  Serial.print("RPM: ");
  Serial.print(rpm);
  Serial.print("\t Status: ");
  
  if (prediction == 0) {
    Serial.println("Normal");
  } else {
    Serial.println(" MISFIRE DETECTED! (Anomaly) ");
  
  delay(100); // Check 10 times a second
}
