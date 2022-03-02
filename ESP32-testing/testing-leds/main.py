from machine import Pin

from time import sleep
led1 = Pin(4, Pin.OUT)
led2 = Pin(5, Pin.OUT)
led3 = Pin(2, Pin.OUT)

while True:
  led1.value(not led1.value())
  sleep(0.1)
  led2.value(not led2.value())
  sleep(0.1)
  led3.value(not led3.value())
  sleep(0.1)