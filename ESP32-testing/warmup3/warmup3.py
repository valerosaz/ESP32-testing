###########################################
# Project integration
# Warmup assignment 3
# ACS students of group 10
# By Phuc Le, Hong Trinh, Shyam Shiwakoti
###########################################
from machine import Pin
# Library for using pin mapping in ESP32
import machine, ssd1306
# Library for OLED display
import time
from time import sleep
import socket
i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0) 
oled.text('Hello', 0, 0)
oled.text('This is group 10', 0, 10)
oled.text('assignment 1', 0, 20)
oled.show()

def web_page():
  if led1.value() == 1:
    Current_state="Blink"
  else:
    Current_state="Stop"
  if led2.value() == 1:
    Current_state="Blink"
  else:
    Current_state="Stop"
  if led3.value() == 1:
    Current_state="Blink"
  else:
    Current_state="Stop"
  
  html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1> 
  <p>GPIO state: <strong>""" + Current_state + """</strong></p><p><a href="/?led=on"><button class="button">ON</button></a></p>
  <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')  
  if led_on == 6:
    print('LED ON')
    while True: 
        led1.value(1)
        sleep(0.1)
        led1.value(0)
        sleep(0.1)
        led2.value(1)
        sleep(0.1)
        led2.value(0)
        sleep(0.1)
        led3.value(1)
        sleep(0.1)
        led3.value(0)
        sleep(0.1)
  if led_off == 6:
    print('LED OFF')
    led3.value(0)
    led2.value(0)
    led1.value(0)
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()