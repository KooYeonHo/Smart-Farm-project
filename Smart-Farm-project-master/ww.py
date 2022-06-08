from flask import Flask, render_template, request
import spidev
import RPi.GPIO as GPIO
import sqlite3
from time import sleep
import db
import threading

class checkThread(threading.Thread):
    
    def __init__(self):
        super().__init__()
                
    def run(self):
        while True:
            data = db.getLastData()
            gwater = data[1]
            if gwater >= 45:
                GPIO.output(6,False)
            else:
                GPIO.output(6,True)
            sleep(1)
        
class dataThread(threading.Thread):
    
    def __init__(self, water, ground, ch1, ch2):
        super().__init__()
        self.water = water
        self.ground = ground
    
    def run(self):
        while True:
            ground_voltage = readAnalog(self.ground, GROUND_WATER_CHANNEL)
            water_voltage = readAnalog(self.water, WATER_CHANNEL)
            ground_percent = 100 - round(ground_voltage,2)
            water_percent = round(water_voltage,2)
            db.insertData(water_percent, ground_percent, 0, 0)

def readAnalog(spi, channel):
  r = spi.xfer2([1, (8 + channel) << 4, 0])
  adc_out = ((r[1]&3) << 8) + r[2]
  return adc_out/10.23

def led_on():
  GPIO.output(20,True)
  
def led_off():
  GPIO.output(20,False)
  
def fan_on():
  GPIO.output(19,True)
  GPIO.output(13,True)

def fan_off():
  GPIO.output(19,False)
  GPIO.output(13,False)

def settings():
  GPIO.setwarnings(False)
  db.setDatabase()
  GPIO.setmode(GPIO.BCM)
  #수중펌프 핀번호 = 6,  환기구 핀번호 = 19,13
  GPIO.setup(19,GPIO.OUT)
  GPIO.setup(6,GPIO.OUT)
  GPIO.setup(13,GPIO.OUT)
  GPIO.setup(20,GPIO.OUT)
  #물 수위 측정 함수
  waterSpi = spidev.SpiDev() 
  waterSpi.open(0,0)
  waterSpi.max_speed_hz = 1000000
  waterSpi.mode = 3

  #토양 수분센서 설정
  groundSpi = spidev.SpiDev()
  groundSpi.open (0, 0)
  groundSpi.mode = 3
  groundSpi.max_speed_hz = 1000000

  
  return waterSpi, groundSpi

    
app = Flask(__name__)
GROUND_WATER_CHANNEL = 0
WATER_CHANNEL = 1


@app.route('/')
def toIndex():
    fan_on()
    data = db.getLastData()
    return render_template("main.html", data=data)

@app.route("/led/on")
def ledOn():
	try:
		led_on()
		return "OK"
	except:
		return "FAIL"

@app.route("/led/off")
def ledOff():
	try:
		led_off()
		return "OK"
	except:
		return "FAIL"

@app.route("/fan/on")
def fanOn():
	try:
		fan_on()
		print("ww")
		return "OK"
	except:
		return "FAIL"

@app.route("/fan/off")
def fanOff():
	try:
		fan_off()
		print("ww")
		return "OK"
	except:
		return "FAIL"


if __name__ == '__main__':
    w,g = settings()
    ch = checkThread()
    th = dataThread(w,g,WATER_CHANNEL,GROUND_WATER_CHANNEL)
    th.start()
    ch.start()
    app.run()
    
    