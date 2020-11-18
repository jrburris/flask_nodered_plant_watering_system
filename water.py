# External module imp
import datetime
import time

import sys
import fake_rpi

sys.modules['RPi'] = fake_rpi.RPi     # Fake RPi
sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO # Fake GPIO
# sys.modules['smbus'] = fake_rpi.smbus # Fake smbus (I2C)

import RPi.GPIO as GPIO


init = False

GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme

def get_last_watered():
    try:
        f = open("last_watered.txt", "r")
        return f.readline()
    except:
        return "NEVER!"
      


def init_output(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    
def auto_water(delay = 5, pump_pin = 7, water_sensor_pin = 8):
    consecutive_water_count = 0
    # init_output(pump_pin)
    print("Here we go! Press CTRL+C to exit")
    try:
        while 1 and consecutive_water_count < 10:
            time.sleep(delay)
            wet = get_status(pin = water_sensor_pin) == 0
            if not wet:
                if consecutive_water_count < 5:
                    pump_on(pump_pin, 1)
                consecutive_water_count += 1
            else:
                consecutive_water_count = 0
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        GPIO.cleanup() # cleanup all GPI

def pump_on(pump_pin = 7, delay = 1):
    init_output(pump_pin)
    f = open("last_watered.txt", "w")
    f.write("Last watered {}".format(datetime.datetime.now()))
    f.close()
    # GPIO.output(pump_pin, GPIO.LOW)
    pump('on', pump_pin)
    time.sleep(1)
    # GPIO.output(pump_pin, GPIO.HIGH)
    pump('off', pump_pin)
    
    

def pump(action, channel):

    # Selecting which GPIO to target
    GPIO_CONTROL = channel
    if action == "on":
        time.sleep(1)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(GPIO_CONTROL, GPIO.OUT)
        GPIO.output(GPIO_CONTROL, True)
    elif action == "off":
        try:
            GPIO.output(GPIO_CONTROL, False)
        except:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(GPIO_CONTROL, GPIO.OUT)
            GPIO.output(GPIO_CONTROL, False)

        GPIO.cleanup()    

def get_status(pin = 8):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN) 
    return GPIO.input(pin)        