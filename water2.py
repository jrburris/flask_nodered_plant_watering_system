# External module imp
import datetime
import time
import sys
import RPi.GPIO as GPIO


pin = 21
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setwarnings(False)
# GPIO.setup(pin, GPIO.OUT)
# GPIO.output(pin, GPIO.LOW)

def get_last_watered():
    try:
        f = open("last_watered.txt", "r")
        return f.readline()
    except:
        return "NEVER!"



def pump_on(delay):

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()



