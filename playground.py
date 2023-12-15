import time

import adafruit_dht
from board import *

while True:
    time.sleep(5)
    for pin in [D4]:
        dht_device = adafruit_dht.DHT22(pin)
        try:
            print(dht_device.temperature)
        except Exception as e:
            print(e)
            continue
