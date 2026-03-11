class BoardSpace:
    occupied: bool

    def __init__(self, rank, file):
        self.rank = rank
        self.file = file
        occupied = False # board space is not occupied by default

class Board:
    