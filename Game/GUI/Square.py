class Square:
    def __init__(self, piece, x, y, covered_by_white=False, covered_by_black=False):
        self.piece = piece
        self.x = x
        self.y = y
        self.covered_by_white = covered_by_white
        self.covered_by_black = covered_by_black

    def get_piece(self):
        return self.piece

    def set_piece(self, piece):
        self.piece = piece

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def is_covered_by_white(self):
        return self.covered_by_white

    def set_covered_by_white(self, covered_by_white):
        self.covered_by_white = covered_by_white

    def is_covered_by_black(self):
        return self.covered_by_black

    def set_covered_by_black(self, covered_by_black):
        self.covered_by_black = covered_by_black

    def get_square(self):
        return [self.x, self.y]
