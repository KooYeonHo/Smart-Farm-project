from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(4, GPIO.OUT)

def fan_on():
    try:
        GPIO.output(4, GPIO.HIGH)
        return True
    except:
        return False
def fan_off():
    try:
        GPIO.output(4, GPIO.LOW)
        return True
    except:
        return False

if __name__ == "__main__":
    while True:
        fan_on()
        sleep(1)
        fan_off()

