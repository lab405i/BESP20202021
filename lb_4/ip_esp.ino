#include <ESP8266WiFi.h>
#include <WiFiClient.h>

#define WIFI_SSID "ssid"                    //ssid of wifi, to which ESP8266 is connected
#define WIFI_PASSWORD "password"            //password of wifi, to which ESP8266 is connected
#define SERVER_IP_ADDRES "255.255.255.255"  //ip addres of server, to which ESP8266 is connected
#define SERVER_PORT 8080                    //port of server, to which ESP8266 is connected
#define DELAY_WIFI_CONNECTION 500           //delay for try connection to wifi in ms
#define DELAY_SERVER_CONNECTION 500         //delay for try connection to server in ms
#define DELAY_LOOP 5                        //delay for loop iteration in ms

WiFiClient esp;

void setup()
{
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN,0);
    WiFi.mode(WIFI_STA);
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
    while (WiFi.status() != WL_CONNECTED) 
    {
        delay(DELAY_WIFI_CONNECTION);
    }
    while(!esp.connect(SERVER_IP_ADDRES,SERVER_PORT))
    {
        delay(DELAY_SERVER_CONNECTION);
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
    delay(DELAY_LOOP);
}
