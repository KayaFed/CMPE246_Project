from config import LED_PINS, USE_HARDWARE

if USE_HARDWARE:
    from led_controller import LEDController
else:
    from mock_led_controller import MockLEDController as LEDController

from time import sleep


def main():
    print("Running LED Test Suite...")
    controller = LEDController(LED_PINS)

    print("Test 1: All LEDs on/off")
    controller.test_all()
    sleep(1)

    print("Test 2: Sweep across board")
    controller.test_sweep()
    sleep(1)

    print("Test 3: Checkerboard pattern")
    controller.test_checkerboard()
    sleep(1)

    print("LED tests complete.")


if __name__ == "__main__":
    main()
