###########################################
# Project integration
# Warmup assignment 3
# ACS students of group 10
# By Phuc Le, Hong Trinh, Shyam Shiwakoti
###########################################
try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network
import time
import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = '((Room_211))-NET_407'
password = 'room2112012'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print('Go to the ESP web server then insert the IP address below to control the LEDs')
print(station.ifconfig())

led1 = Pin(12, Pin.OUT)
led2 = Pin(13, Pin.OUT)
led3 = Pin(14, Pin.OUT)
