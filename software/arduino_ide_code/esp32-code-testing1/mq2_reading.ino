#include <WiFi.h>
#include <HTTPClient.h>
const char* ssid = "YOUR_WIFI_NAME";
const char* password = "YOUR_WIFI_PASSWORD";
const char* serverName = "http://YOUR_LOCAL_IP:5000/predict";
const int mq2Pin = 34;

void setup() {
  Serial.begin(115200);
  delay(1000);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi connected");
}

void loop() {
  int mq2Value = analogRead(mq2Pin);

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");

    String jsonData = "{\"mq2\":" + String(mq2Value) + "}";

    int responseCode = http.POST(jsonData);

    if (responseCode > 0) {
      String response = http.getString();
      Serial.println(response);
    } else {
      Serial.print("HTTP Error: ");
      Serial.println(responseCode);
    }

    http.end();
  }

  delay(4000);
}
