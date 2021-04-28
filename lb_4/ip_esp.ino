#include <ESP8266WiFi.h>
#include <WiFiClient.h>

#define WIFI_SSID "Attack_Helicopter"
#define WIFI_PASSWORD "19861986"
#define SERVER_IP_ADDRES "255.255.255.255"
#define SERVER_PORT 8080

WiFiClient esp;

void setup()
{
    Serial.begin(9600);
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN,0);
    WiFi.mode(WIFI_STA);
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
    while (WiFi.status() != WL_CONNECTED) 
    {
        delay(500);
    }
    while(!esp.connect(SERVER_IP_ADDRES,SERVER_PORT))
    {
        delay(500);
    }
}

void loop()
{
    while(esp.available())
    {
        String mgs = esp.readString();
        if (mgs == "on\n")
        {
            digitalWrite(LED_BUILTIN,1);
        }
        else if (mgs == "off\n")
        {
            digitalWrite(LED_BUILTIN,0);
        }
    }
    delay(10);
}
