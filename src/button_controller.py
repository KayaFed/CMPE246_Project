# src/button_controller.py

try:
    from gpiozero import Button
except ImportError:
    Button = None  # Allows Windows simulation

class ButtonController:
    def __init__(self, pin):
        if Button is None:
            raise RuntimeError("gpiozero not available — must run on Raspberry Pi")

        self.button = Button(pin)

    def wait_for_press(self):
        """Block until the button is pressed."""
        print("Waiting for button press...")
        self.button.wait_for_press()
        print("Button pressed!")
