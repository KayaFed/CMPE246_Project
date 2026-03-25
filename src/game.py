# game.py

import chess

class Game:
    def __init__(self, controller):
        self.controller = controller

    def highlight_move(self, move_uci):
        """
        Takes a UCI move like 'e2e4' and lights up the LEDs
        for the from-square and to-square.
        """

        # Convert UCI string to a python-chess Move object
        move = chess.Move.from_uci(move_uci)

        # Convert squares to LED indices (0–63)
        from_index = move.from_square
        to_index = move.to_square

        print(f"Highlighting move: {move_uci}")
        print(f"From index: {from_index}, To index: {to_index}")

        # Light up LEDs
        self.controller.turn_on(from_index)
        self.controller.turn_on(to_index)
