# flask_web_plant


### Acknowledgements
This project is based on the work done here http://www.cyber-omelette.com/2017/09/automated-plant-watering.html


### Scheduling
$> sudo crontab -e

@reboot cd <your path to plant_app>; sudo python3 plant_app.py


# Senors
* Adafruit STEMMA Soil Sensor - I2C Capacitive Moisture Sensor
sudo pip3 install adafruit-circuitpython-seesaw

# Wiring setup
### Adafruit STEMMA Soil Sensor - I2C Capacitive Moisture Sensor
1. Pi 3V3 (Pin 1) to sensor VIN (Red)
2. Pi SDA (Pin 3) to sensor SDA (White)
3. Pi SCL (Pin 5) to sensor SCL (Green)
4. Pi GND (Pin 9) to sensor GND (Black)


# Node-Red
```
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
```
npm install node-red-dashboard

