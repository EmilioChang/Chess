from .Piece import Piece
from ..GUI import Utils

class Knight(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)

    def piece_image(self):
        if self.is_white:
            return Utils.pieces["wn"]
        else:
            return Utils.pieces["bn"]
        
    def piece_notation(self):
        return "N"

    def move(self, initial_square, destination_square):
        dx, dy = self.dxdy(initial_square, destination_square)

        return not self.has_friendly_piece(destination_square) and (dx * dy == 2)