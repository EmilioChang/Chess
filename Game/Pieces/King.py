from .Piece import Piece
from ..GUI import Utils

class King(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)
        self.can_castle = True

    def piece_image(self):
        if self.is_white:
            return Utils.pieces["wk"]
        else:
            return Utils.pieces["bk"]
        
    def piece_notation():
        return "K"

    def move(self, board, initial_square, destination_square):
        if self.has_friendly_piece(destination_square):
            return False
        
        dx, dy = self.dxdy(initial_square, destination_square)
        
        if dx > 1 or dy > 1:
            return False
        
        if self.is_white:
            return not destination_square.is_covered_by_black
        else:
            return not destination_square.is_covered_by_white
    
    def castle(self):
        # TODO
        self.can_castle = False