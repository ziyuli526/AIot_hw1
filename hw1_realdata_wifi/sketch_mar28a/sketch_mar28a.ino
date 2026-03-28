#include "DHT.h"
#include <WiFi.h>
#include <HTTPClient.h>

#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// ===== 請修改這三個地方 =====
const char* ssid = "ziyu (2)";
const char* password = "1234567890";
const char* serverURL = "http://172.20.10.19:5000/sensor";
// ===========================

void setup() {
  Serial.begin(9600);
  dht.begin();
  
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi Connected!");
  Serial.println(WiFi.localIP());
}

void loop() {
  delay(2000);
  
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  
  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverURL);
    http.addHeader("Content-Type", "application/json");
    
    String payload = "{\"temperature\":" + String(t) + 
                     ",\"humidity\":" + String(h) + 
                     ",\"rssi\":" + String(WiFi.RSSI()) + "}";
    
    int httpCode = http.POST(payload);
    Serial.println("Sent: " + payload);
    Serial.println("Response: " + String(httpCode));
    http.end();
  }
  
  delay(3000); // 每5秒送一次
}