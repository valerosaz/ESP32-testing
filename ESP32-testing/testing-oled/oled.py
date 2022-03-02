import machine, ssd1306
i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))

oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0) 
oled.text('Hallo', 0, 0)
oled.text('Ik ben Phuc', 0, 10)
oled.text('Welkom', 0, 20)
oled.show()
