import spidev
import RPi.GPIO as GPIO
import sqlite3
from time import sleep
import db

def readAnalog(spi, channel):
  r = spi.xfer2([1, (8 + channel) << 4, 0])
  adc_out = ((r[1]&3) << 8) + r[2]
  return adc_out/10.23

def fan_on():
  GPIO.output(19,True)
  GPIO.output(13,True)

def fan_off():
  GPIO.output(19,False)
  GPIO.output(13,False)
  
def led_on():
  GPIO.output(20,True)
  
def led_off():
  GPIO.output(20,False)
  
def settings():
  db.setDatabase()
  GPIO.setmode(GPIO.BCM)
  #수중펌프 핀번호 = 6,  환기구 핀번호 = 19,13  led 핀번호 = 20
  GPIO.setup(20,GPIO.OUT)
  GPIO.setup(19,GPIO.OUT)
  GPIO.setup(6,GPIO.OUT)
  GPIO.setup(13,GPIO.OUT)

  #물 수위 측정 함수
  waterSpi = spidev.SpiDev() 
  waterSpi.open(0,0)
  waterSpi.max_speed_hz = 1000000
  waterSpi.mode = 3
  WATER_CHANNEL = 0

  #토양 수분센서 설정
  groundSpi = spidev.SpiDev()
  groundSpi.open (0, 0)
  groundSpi.mode = 3
  groundSpi.max_speed_hz = 1000000
  GROUND_WATER_CHANNEL = 1

  while True:
    ground_voltage = readAnalog(groundSpi, GROUND_WATER_CHANNEL)
    water_voltage = readAnalog(waterSpi, WATER_CHANNEL)
    ground_percent = 100 - round(ground_voltage,2)
    water_percent = round(water_voltage,2)
    db.insertData(water_percent, ground_percent, 0, 0) 
    sleep(1)
    

