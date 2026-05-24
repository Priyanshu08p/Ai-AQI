#include <WiFi.h>
const int mq2Pin = 34;
void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("MQ-2 Sensor Starting...");
}
void loop() {
  int gasValue = analogRead(mq2Pin);
  Serial.print("Gas Value: ");
  Serial.println(gasValue);

  delay(1000);
}
