import time
import board
import busio
from adafruit_mcp230xx.mcp23017 import MCP23017

def main():
    print("Starting MCP23017 Reed Test (32 inputs, 2 expanders)...")

    # Initialize I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # I2C addresses for the two expanders
    ADDRESS_1 = 0x20   # First MCP23017
    ADDRESS_2 = 0x21   # Second MCP23017 (A0 jumper set)

    # Create MCP23017 instances
    mcp1 = MCP23017(i2c, address=ADDRESS_1)
    mcp2 = MCP23017(i2c, address=ADDRESS_2)

    # Configure all 32 pins as inputs with pull-ups
    pins = []

    # First expander: pins 0–15
    for i in range(16):
        pin = mcp1.get_pin(i)
        pin.switch_to_input(pull_up=True)
        pins.append(pin)

    # Second expander: pins 16–31
    for i in range(16):
        pin = mcp2.get_pin(i)
        pin.switch_to_input(pull_up=True)
        pins.append(pin)

    print("Reading 32 reed switches... Press Ctrl+C to stop.")

    while True:
        # MCP23017 pin.value = True when open, False when closed
        # We invert it so: True = magnet present
        states = [not pin.value for pin in pins]

        print(states)
        time.sleep(0.3)

if __name__ == "__main__":
    main()
