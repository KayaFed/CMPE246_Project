# Allows to test withough having LEDs hooked up
# When LED gets hoked up: Replace GPIO in main to hook up with lights.
# ------------------------
# In main replace: 
# from led_controller import LEDController
#from mock_led_controller import MockLEDController as LEDController
# ------------------------
# src/mock_led_controller.py

class MockLEDController:
    def __init__(self, pins):
        self.pins = pins

    def turn_on(self, index):
        print(f"[LED ON] Index: {index}")

    def turn_off(self, index):
        print(f"[LED OFF] Index: {index}")

    def all_on(self):
        print("[ALL LEDs ON]")

    def all_off(self):
        print("[ALL LEDs OFF]")

    def set_square(self, row, col):
        index = row * 8 + col
        self.turn_on(index)

    def clear_square(self, row, col):
        index = row * 8 + col
        self.turn_off(index)