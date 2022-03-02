###########################################
# Project integration
# Warmup assignment 1
# ACS students of group 10
# By Phuc Le, Hong Trinh, Shyam Shiwakoti
###########################################
from machine import Pin
# Library for using pin mapping in ESP32
import machine, ssd1306
# Library for OLED display
from time import sleep
i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0) 
oled.text('Hallo', 0, 0)
oled.text('Ik ben Groep 10', 0, 10)
oled.text('opwarmen 1', 0, 20)
oled.show()

led1 = Pin(12, Pin.OUT)
led2 = Pin(13, Pin.OUT)
led3 = Pin(14, Pin.OUT)

while True:
  led1.value(not led1.value())
  sleep(0.1)
  led2.value(not led2.value())
  sleep(0.1)
  led3.value(not led3.value())
  sleep(0.1)