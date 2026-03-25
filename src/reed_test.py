# src/reed_test.py

from config import REED_PINS, USE_HARDWARE

if USE_HARDWARE:
    from reed_controller import ReedController
else:
    from mock_reed_controller import MockReedController as ReedController

from time import sleep


def main():
    print("Starting Reed Switch Test...")
    reeds = ReedController(REED_PINS)

    while True:
        state = reeds.read_raw()
        print(state)
        sleep(0.5)


if __name__ == "__main__":
    main()
