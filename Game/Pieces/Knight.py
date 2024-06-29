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

    def move(self, initial_square, destination_square):
        if destination_square.piece and destination_square.piece.is_white == self.is_white:
            return False
        
        dx = abs(initial_square.x - destination_square.x)
        dy = abs(initial_square.y - destination_square.y)

        if dx * dy != 2:
            return False
        
        return True