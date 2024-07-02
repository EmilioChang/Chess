class Square:
    def __init__(self, piece, x, y, covered_by_white=False, covered_by_black=False):
        self.piece = piece
        self.x = x
        self.y = y
        self.covered_by_white = covered_by_white
        self.covered_by_black = covered_by_black