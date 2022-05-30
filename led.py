import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT)
try:
    while True:
        GPIO.output(20,True)
        sleep(5)
        GPIO.output(20,False)
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()