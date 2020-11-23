# External module imp
import datetime
import time
import sys
import RPi.GPIO as GPIO

init = False

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

def get_last_watered():
    try:
        f = open("last_watered.txt", "r")
        return f.readline()
    except:
        return "NEVER!"
      

def init_output(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    

def pump_on(pump_pin = 4, delay = 1):
    init_output(pump_pin)
    f = open("last_watered.txt", "w")
    f.write("{}".format(datetime.datetime.now()))
    f.close()
    # GPIO.output(pump_pin, GPIO.LOW)
    pump('on', pump_pin)
    time.sleep(1)
    # GPIO.output(pump_pin, GPIO.HIGH)
    pump('off', pump_pin)
    

def pump(action, pump_pin):

    # Selecting which GPIO to target
    GPIO_CONTROL = pump_pin
    if action == "on":
        time.sleep(1)
        # GPIO.setmode(GPIO.BOARD)
        GPIO.setup(GPIO_CONTROL, GPIO.OUT)
        GPIO.output(GPIO_CONTROL, True)
    elif action == "off":
        try:
            GPIO.output(GPIO_CONTROL, False)
        except:
            # GPIO.setmode(GPIO.BOARD)
            GPIO.setup(GPIO_CONTROL, GPIO.OUT)
            GPIO.output(GPIO_CONTROL, False)

        GPIO.cleanup()    

# def get_status(pin = 8):
#     GPIO.setmode(GPIO.BOARD)
#     GPIO.setup(pin, GPIO.IN) 
#     return GPIO.input(pin)        