import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
##fan = 19,13
##water = 6
GPIO.setup(19,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
try:
    while True:
        GPIO.output(19,True)
        GPIO.output(13,True)
        GPIO.output(20,True)
        sleep(5)
        GPIO.output(19,False)
        GPIO.output(13,False)
        GPIO.output(20,False)
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()