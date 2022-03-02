###########################################
# Project integration
# Warmup assignment 4
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

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ESP32-G10')
ap.config(authmode=3, password='phucle1112')

#esp.osdebug(None)
#
#import gc
#gc.collect()
#
#ssid = 'PhucLE_com'
#password = 'phucle1112'
#
#station = network.WLAN(network.STA_IF)
#
#station.active(True)
#station.connect(ssid, password)
#
#while station.isconnected() == False:
#  pass
