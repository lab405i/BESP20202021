import RPi.GPIO as GPIO
from time import sleep
 
RED_PIN = 36
YELLOW_PIN = 32
GREEN_PIN = 29
BUTTON_PIN = 40

print ("RPi.GPIO init start")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
print ("RPi.GPIO init end")

print ("GPIO setup")
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(RED_PIN, 0)
GPIO.output(YELLOW_PIN, 0)
GPIO.output(GREEN_PIN, 1)

 
while True:
    inp = GPIO.input(BUTTON_PIN)
    if inp==0:
       for x in range(0, 5):
           GPIO.output(GREEN_PIN, 1)
           sleep(0.5)
           GPIO.output(GREEN_PIN, 0)
           sleep(0.5)
       GPIO.output(YELLOW_PIN, 1)
       sleep(2)
       GPIO.output(YELLOW_PIN, 0)
       GPIO.output(RED_PIN, 1)
       sleep(5)
       GPIO.output(YELLOW_PIN, 1)
       sleep(1)
   

       GPIO.output(RED_PIN, 0)
       GPIO.output(YELLOW_PIN, 0)
       GPIO.output(GREEN_PIN, 1)

