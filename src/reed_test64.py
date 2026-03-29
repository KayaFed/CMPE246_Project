import time
import board
import busio
from adafruit_mcp230xx.mcp23017 import MCP23017

repeat = True
def main():
    print("Starting MCP23017 Reed Test (64 inputs, 4 expanders)...")

    # Initialize I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # I2C addresses for the two expanders
    ADDRESS_1 = 0x20   # First MCP23017
    ADDRESS_2 = 0x21
    ADDRESS_3 = 0x22  # Second MCP23017 (A0 jumper set)
    ADDRESS_4 = 0x23  # Third MCP23017 (A0 and A1 jumpers set)

    # Create MCP23017 instances
    mcp1 = MCP23017(i2c, address=ADDRESS_1)
    mcp2 = MCP23017(i2c, address=ADDRESS_2)
    mcp3 = MCP23017(i2c, address=ADDRESS_3)
    mcp4 = MCP23017(i2c, address=ADDRESS_4)

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

    # Third expander: pins 32–47
    for i in range(16):
        pin = mcp3.get_pin(i)
        pin.switch_to_input(pull_up=True)
        pins.append(pin)

    # Fourth expander: pins 48–63
    for i in range(16):
        pin = mcp4.get_pin(i)
        pin.switch_to_input(pull_up=True)
        pins.append(pin)

    print("Reading 64 reed switches... Press Ctrl+C to stop.")

    while repeat:
        # MCP23017 pin.value = True when open, False when closed
        # We invert it so: True = magnet present
        states = [not pin.value for pin in pins]

        print(states)
        time.sleep(0.3)
        repeat = False

if __name__ == "__main__":
    main()
