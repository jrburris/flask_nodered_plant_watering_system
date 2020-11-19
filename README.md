# flask_web_plant


### Acknowledgements
This project is based on the work done here http://www.cyber-omelette.com/2017/09/automated-plant-watering.html


### Scheduling
$> sudo crontab -e

@reboot cd <your path to web_plants>; sudo python3 web_plants.py


# Senors
### Adafruit STEMMA Soil Sensor - I2C Capacitive Moisture Sensor

# Wiring setup
### Adafruit STEMMA Soil Sensor - I2C Capacitive Moisture Sensor
1. Pi 3V3 (Pin 1) to sensor VIN (Red)
2. Pi SDA (Pin 3) to sensor SDA (White)
3. Pi SCL (Pin 5) to sensor SCL (Green)
4. Pi GND (Pin 9) to sensor GND (Black)

