import os, sys
print("CWD:", os.getcwd())
print("PATH:", sys.path)

from config import LED_PINS, USE_HARDWARE, BUTTON_PIN
import config  # for debugging

# LED controller selection
if USE_HARDWARE:
    from led_controller import LEDController
else:
    from mock_led_controller import MockLEDController as LEDController

# Button controller selection
if USE_HARDWARE:
    from button_controller import ButtonController
else:
    from mock_button_controller import MockButtonController as ButtonController

from game import Game
from engine import ChessEngine
from time import sleep


def main():
    mode = "HARDWARE" if USE_HARDWARE else "SIMULATION"
    print(f"Starting Chess Board System ({mode} Mode)...")

    # Debug info
    print("Loaded config from:", config.__file__)
    print("LED_PINS length:", len(LED_PINS))

    controller = LEDController(LED_PINS)
    button = ButtonController(BUTTON_PIN)
    game = Game(controller)
    engine = ChessEngine()

    try:
        while True:
            # Wait for player to confirm their move
            button.wait_for_press()

            # Engine generates a move
            move = engine.get_best_move()
            print("Engine move:", move)

            # Highlight move on LEDs
            game.highlight_move(move)

            # Optional: print board state
            print(engine.board)

            sleep(1)

    except KeyboardInterrupt:
        print("\nStopping program...")

    finally:
        engine.close()


if __name__ == "__main__":
    main()
