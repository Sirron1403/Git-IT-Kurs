from gpiozero import LED, Button
import time
import sqlite3

class ORM:
    def __init__(self,file_name):
        db = sqlite3.connect("setup_led.db")
        self.connection = sqlite3.connect(file_name)
        self.cursor = self.connection.cursor()
        self.save_time = time.time()
    
    def save_time(self,Zeitstempel, Led_active):
        self.cursor.execute("INSERT INTO setupled(Zeitstempel, led_active) VALUES (?, ?)", (Zeitstempel, Led_active))
        self.connection.commit()

    def close(self):
        self.connection.close()

class LED:
    def __init__(self, pin):
        self.pin = pin
        self.led = LED(pin)
        self.led.off()

    def led_on(self):
        self.led.on()

    def led_off(self):
        self.led.off()

class Taster:
    def __init__(self, pin):
        self.pin = pin
        self.taster = Button(pin)

    def is_pressed(self):
        return self.taster.is_pressed

class Main:
    def __init_(self):
        self.led = LED(17)
        self.taster = Taster(2)
        self.Orm = ORM("setup_led.db")
    
    def is_pressed(self):
        return self.taster.is_pressed
    
    def button_realesed(self):
        return not self.taster.is_pressed
