from flask import Flask, render_template, redirect, url_for, jsonify
import psutil
import datetime
import time
import water2
import os
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw
import RPi.GPIO as GPIO

i2c_bus = busio.I2C(SCL, SDA)
ss = Seesaw(i2c_bus, addr=0x36)

app = Flask(__name__)


@app.route("/soil_sensor")
def get_soil_sensor():
    responce = {'temp': '','moisture': ''}

    # read moisture level through capacitive touch pad
    responce['moisture'] = ss.moisture_read()
    # read temperature from the temperature sensor
    fahrenheit = (ss.get_temp() * 9/5) + 32
    responce['temp'] = round(fahrenheit, 2)

    return jsonify(responce)


@app.route("/water")
def action2():
    water2.pump_on()
    responce = {'status': 'done', 'last_watered': "{}".format(datetime.datetime.now())}
    return jsonify(responce)


@app.route("/last_watered")
def check_last_watered():
    text = water2.get_last_watered()
    reponce = {'last_watered': text}
    return jsonify(reponce)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)