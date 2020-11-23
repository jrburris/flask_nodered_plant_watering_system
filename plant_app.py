from flask import Flask, render_template, redirect, url_for, jsonify
import psutil
import datetime
import time
# import water
import os
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT, initial = GPIO.LOW)



i2c_bus = busio.I2C(SCL, SDA)
ss = Seesaw(i2c_bus, addr=0x36)


app = Flask(__name__)

# def template(title = "Plant Helpline!", text = ""):
#     now = datetime.datetime.now()
#     timeString = now
#     templateDate = {
#         'title' : title,
#         'time' : timeString,
#         'text' : text
#         }
#     return templateDate

# @app.route("/")
# def hello():
#     templateData = template()
#     return render_template('main.html', **templateData)

@app.route("/soil_sensor")
def get_soil_sensor():
    responce = {'temp': '','moisture': ''}

    # read moisture level through capacitive touch pad
    responce['moisture'] = ss.moisture_read()
    # read temperature from the temperature sensor
    fahrenheit = (ss.get_temp() * 9/5) + 32
    responce['temp'] = round(fahrenheit, 2)

    return jsonify(responce)



# @app.route("/last_watered")
# def check_last_watered():
#     try:
#         f = open("last_watered.txt", "r")
#         return f.readline()
#     except:
#         return "NEVER!"

# @app.route("/sensor")
# def action():
#     status = water.get_status()
#     message = ""
#     if (status == 1):
#         message = "Water me please!"
#     else:
#         message = "I'm a happy plant"

#     templateData = template(text = message)
#     return render_template('main.html', **templateData)

@app.route("/water")
def action2():

    f = open("last_watered.txt", "w")
    f.write("Last watered {}".format(datetime.datetime.now()))
    f.close()
    time.sleep(1)
    GPIO.output(4, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(4, GPIO.LOW)
    time.sleep(1)

    responce = {'status': 'ok'}

    return jsonify(responce)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)