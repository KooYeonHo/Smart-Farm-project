import spidev
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
#물 수위 측정 함수
spi = spidev.SpiDev() 
spi.open(0,0)
spi.max_speed_hz = 1000000
spi.mode = 3
WATER_CHANNEL = 0

#물 수위 측정 
def readAnalog(channel):
  r = spi.xfer2([1, (8 + channel) << 4, 0])
  adc_out = ((r[1]&3) << 8) + r[2]
  return adc_out/10.23

##토양 수분센서
spi = spidev.SpiDev()
spi.open (0, 0)
spi.mode = 3
spi.max_speed_hz = 1000000

def read_spi_adc(channel):
  adcValue = 0
  buff = spi.xfer2([1,(8+channel)<< 4,0])
  adcValue = ((buff[1] & 3) << 8)+buff[2]
  return (adcValue/10.23)

while True:
    ground_voltage = read_spi_adc(0)
    water_voltage = readAnalog(1)
    ground_percent = str(100 - round(ground_voltage,2))
    water_percent = str(round(water_voltage,2))
    print("ground water: " + ground_percent)
    print("water percent: " + water_percent)
    sleep(1)