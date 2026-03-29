import time
import board
import busio
from adafruit_mcp230xx.mcp23017 import MCP23017

def main():
    print("Starting MCP23017 Reed Test (16 inputs)...")

    # Initialize I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # Your confirmed MCP23017 I2C address
    ADDRESS = 0x20

    # Create MCP23017 instance
    mcp = MCP23017(i2c, address=ADDRESS)

    # Configure all 16 pins as inputs with pull-ups
    pins = []
    for i in range(16):
        pin = mcp.get_pin(i)
        pin.switch_to_input(pull_up=True)
        pins.append(pin)

    print("Reading reed switches... Press Ctrl+C to stop.")

    while True:
        # MCP23017 pin.value = True when open, False when closed
        # We invert it so: True = magnet present
        states = [not pin.value for pin in pins]

        print(states)
        time.sleep(0.3)

if __name__ == "__main__":
    main()
