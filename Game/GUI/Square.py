class Square:
    def __init__(self, name, piece, x, y, is_covered_by_white=False, is_covered_by_black=False):
        self.name = name
        self.piece = piece
        self.x = x
        self.y = y
        self.is_covered_by_white = is_covered_by_white
        self.is_covered_by_black = is_covered_by_black