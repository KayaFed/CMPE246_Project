# src/led_controller.py

try:
    from gpiozero import LED
except ImportError:
    LED = None  # Allows this file to exist on Windows without crashing


class LEDController:
    def __init__(self, pins):
        if LED is None:
            raise RuntimeError("gpiozero not available — must run on Raspberry Pi")

        # Create LED objects for each pin
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
    def test_single(self, index, delay=0.2):
        """Turn on one LED briefly for wiring verification."""
        self.turn_on(index)
        sleep(delay)
        self.turn_off(index)

    def test_all(self, delay=0.5):
        """Turn all LEDs on, then off."""
        self.all_on()
        sleep(delay)
        self.all_off()

    def test_sweep(self, delay=0.05):
        """Light each LED in order, one at a time."""
        for i in range(len(self.leds)):
            self.test_single(i, delay)

    def test_checkerboard(self, delay=1):
        """Alternate LEDs in a checkerboard pattern."""
        for i in range(len(self.leds)):
            if (i + (i // 8)) % 2 == 0:
                self.turn_on(i)
            else:
                self.turn_off(i)
        sleep(delay)
        self.all_off()
