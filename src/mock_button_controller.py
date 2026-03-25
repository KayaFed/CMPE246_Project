# src/mock_button_controller.py

class MockButtonController:
    def __init__(self, pin):
        self.pin = pin

    def wait_for_press(self):
        """Simulate a button press by waiting for Enter."""
        input("Press ENTER to simulate button press...")
