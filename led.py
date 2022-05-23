import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
pwm = GPIO.PWM(21, 3000)
pwm.start(0)
duty = 0
try:
    while True:
        pwm.ChangeDutyCycle(duty)
        duty = 100
        sleep(0.5)
        print(duty)
        if(duty == 100):
            duty=0
except KeyboardInterrupt:
    GPIO.cleanup()
    pwm.stop()