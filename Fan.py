from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setwarnings(False)




def fan_on():
    try:
        GPIO.output(26, GPIO.HIGH)
        return True
    except:
        return False
def fan_off():
    try:
        GPIO.output(26, GPIO.LOW)
        return True
    except:
        return False

if __name__ == "__main__":
    while True:
        fan_on()
        print("si hang jung")
        sleep(1)
        fan_off()

