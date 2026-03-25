Once LEDs are hooked up and the controller can be updated, LED Controller will be updated into:



# src/led_controller.py
from gpiozero import LED

class LEDController:
    def __init__(self, pins):
        self.leds = [LED(pin) for pin in pins]

    def turn_on(self, index):
        self.leds[index].on()

    def turn_off(self, index):
        self.leds[index].off()

    def all_on(self):
        for led in self.leds:
            led.on()

    def all_off(self):
        for led in self.leds:
            led.off()
