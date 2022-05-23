import spidev
import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
DIGIT = 23
GPIO.setup(DIGIT,GPIO.IN)
spi = spidev.SpiDev()
spi.open (0, 0)
spi.mode = 3
spi.max_speed_hz = 1000000

def read_spi_adc(channel):
  adcValue = 0
  buff = spi.xfer2([1,(8+channel)<< 4,0])
  adcValue = ((buff[1] & 3) << 8)+buff[2]
  return (adcValue/10)

while True:
    voltage = read_spi_adc(1)*3.3/1024
    print(voltage)
    sleep(1)