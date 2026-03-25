import os, sys
print("CWD:", os.getcwd())
print("PATH:", sys.path)

from config import LED_PINS, USE_HARDWARE
import config  # for debugging

# Choose LED controller based on hardware/simulation mode
if USE_HARDWARE:
    from led_controller import LEDController
else:
    from mock_led_controller import MockLEDController as LEDController

from game import Game
from engine import ChessEngine
from time import sleep


def main():
    mode = "HARDWARE" if USE_HARDWARE else "SIMULATION"
    print(f"Starting Chess Board System ({mode} Mode)...")

    # Debug: confirm config file and LED_PINS
    print("Loaded config from:", config.__file__)
    print("LED_PINS length:", len(LED_PINS))

    controller = LEDController(LED_PINS)
    game = Game(controller)
    engine = ChessEngine()  # Make sure Stockfish path is correct if needed

    try:
        while True:
            # Get move from engine
            move = engine.get_best_move()
            print("Engine move:", move)

            # Highlight move on board (LEDs)
            game.highlight_move(move)

            # Optional: print board state
            print(engine.board)

            sleep(2)

    except KeyboardInterrupt:
        print("\nStopping program...")

    finally:
        engine.close()


if __name__ == "__main__":
    main()
