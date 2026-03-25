# src/mock_reed_controller.py

class MockReedController:
    def __init__(self, pins):
        self.pins = pins
        self.state = [False] * len(pins)

    def read_raw(self):
        """
        Simulate reed switches by printing the current state.
        You can manually edit self.state during testing.
        """
        print("Mock reed state:", self.state)
        return self.state
