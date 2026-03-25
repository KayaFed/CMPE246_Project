from gpiozero import LED
from time import sleep
from config import LED_PINS

# Create LED objects
leds = [LED(pin) for pin in LED_PINS]

def test_all_on():
    print("Turning ALL LEDs ON")
    for led in leds:
        led.on()
    sleep(2)

def test_all_off():
    print("Turning ALL LEDs OFF")
    for led in leds:
        led.off()
    sleep(2)

def test_sequence():
    print("Running LED sequence...")
    for i, led in enumerate(leds):
        print(f"LED {i} ON")
        led.on()
        sleep(0.5)
        led.off()

if __name__ == "__main__":
    test_all_on()
    test_all_off()
    test_sequence()