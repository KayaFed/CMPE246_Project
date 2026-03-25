# src/reed_controller.py

try:
    from gpiozero import InputDevice
except ImportError:
    InputDevice = None  # Allows Windows simulation


class ReedController:
    def __init__(self, pins):
        if InputDevice is None:
            raise RuntimeError("gpiozero not available — must run on Raspberry Pi")

        # Create an InputDevice for each reed switch pin
        self.sensors = [InputDevice(pin, pull_up=True) for pin in pins]

    def read_raw(self):
        """
        Returns a list of booleans representing each reed switch.
        True  = magnet present (piece on square)
        False = no magnet
        """
        return [not sensor.value for sensor in self.sensors]  
        # gpiozero InputDevice.value is 1 when open, 0 when closed
