#include <WiFi.h>
#include <HTTPClient.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// WiFi credentials
const char* ssid = "YOUR_WIFI_NAME";
const char* password = "YOUR_WIFI_PASSWORD";

// Flask server
const char* serverName = "http://YOUR_LOCAL_IP:5000/predict";

// MQ2 sensor pin
const int mq2Pin = 34;

// LCD (I2C Address: 0x27)
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {

  Serial.begin(115200);
  delay(1000);

  lcd.init();
  lcd.backlight();

  lcd.setCursor(0, 0);
  lcd.print("Starting...");

  WiFi.begin(ssid, password);

  lcd.setCursor(0, 1);
  lcd.print("Connecting...");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi Connected");

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("WiFi Connected");

  delay(2000);
}

void loop() {

  int mq2Value = analogRead(mq2Pin);

  Serial.print("MQ2 Value: ");
  Serial.println(mq2Value);

  if (WiFi.status() == WL_CONNECTED) {

    HTTPClient http;

    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");

    String jsonData = "{\"mq2\":" + String(mq2Value) + "}";

    int responseCode = http.POST(jsonData);

    if (responseCode > 0) {

      String response = http.getString();

      Serial.println(response);

      int aqiIndex = response.indexOf("aqi");
      int colon = response.indexOf(":", aqiIndex);
      int comma = response.indexOf(",", colon);

      float aqiValue = response.substring(colon + 1, comma).toFloat();

      int catIndex = response.indexOf("category");
      int colon2 = response.indexOf(":", catIndex);
      int quote1 = response.indexOf("\"", colon2 + 1);
      int quote2 = response.indexOf("\"", quote1 + 1);

      String category = response.substring(quote1 + 1, quote2);

      lcd.clear();

      lcd.setCursor(0, 0);
      lcd.print("AQI: ");
      lcd.print(aqiValue);

      lcd.setCursor(0, 1);
      lcd.print(category);

    } else {

      Serial.print("HTTP Error: ");
      Serial.println(responseCode);

      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Server Error");
    }

    http.end();
  }

  delay(4000);
}
