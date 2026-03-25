# engine.py

import chess
import chess.engine

class ChessEngine:
    def __init__(self):
        self.board = chess.Board()

        # Path to your Stockfish executable
        self.engine = chess.engine.SimpleEngine.popen_uci(
            "C:/Users/Kaya/OneDrive/Documents/chess_engine/stockfish/stockfish-windows-x86-64-avx2.exe"
        )

    def get_best_move(self):
        result = self.engine.play(self.board, chess.engine.Limit(time=0.1))
        move = result.move
        self.board.push(move)
        return move.uci()

    def close(self):
        self.engine.quit()
