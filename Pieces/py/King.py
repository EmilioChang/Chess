import Piece

class King(Piece):
    can_castle = True

    def __init__(self, is_white):
        super().__init__(is_white)

    def move(self, initial_square, destination_square):
        # TODO: Implement castling
        if destination_square.piece and destination_square.piece.is_white == self.is_white:
            return False
        
        dx = abs(initial_square.x - destination_square.x)
        dy = abs(initial_square.y - destination_square.y)
        
        if dx > 1 or dy > 1:
            return False
        
        if self.is_white:
            if destination_square.is_covered_by_black():
                return False
        else:
            if destination_square.is_covered_by_white():
                return False
        
        return True
    
    def castle(self):
        self.can_castle = False