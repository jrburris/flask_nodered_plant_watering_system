import RPi.GPIO as GPIO
import time


channel = 4

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(channel, GPIO.OUT)

def pump(action):

    # Selecting which GPIO to target
    GPIO_CONTROL = channel
    if action == "on":
        time.sleep(1)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_CONTROL, GPIO.OUT)
        GPIO.output(GPIO_CONTROL, True)
    elif action == "off":
        try:
            GPIO.output(GPIO_CONTROL, False)
        except:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(GPIO_CONTROL, GPIO.OUT)
            GPIO.output(GPIO_CONTROL, False)

        GPIO.cleanup()



if __name__ == '__main__':
    try:
        pump('on')  # Turn motor on
        time.sleep(1)
        pump('off')  # Turn motor off
        time.sleep(1)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()
