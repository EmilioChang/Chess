from .Piece import Piece
from ..GUI import Utils
from ..GUI import Square

class King(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)
        self.can_castle = True

    def piece_image(self):
        if self.is_white:
            return Utils.pieces["wk"]
        else:
            return Utils.pieces["bk"]
        
    def piece_notation(self):
        return "K"

    def move(self, board, initial_square, destination_square):
        status = None
        dx, dy = self.dxdy(initial_square, destination_square)

        if self.has_friendly_piece(destination_square):
            status = False
        elif dx > 1:
            status = False
        elif dy == 2:
            status = self.castle(board, initial_square, destination_square)
        elif dy > 2:
            status = False
        elif self.is_white:
            status = not destination_square.is_covered_by_black
        else:
            status = not destination_square.is_covered_by_white

        self.can_castle = False

        return status
    
    def castle(self, board, initial_square, destination_square):
        if not self.can_castle:
            return False

        if initial_square.x != destination_square.x:
            return False
        

        x = initial_square.x
        y = initial_square.y
        y_castling_direction = (3 if initial_square.y < destination_square.y else -4) + y

        piece = board[x][y_castling_direction].piece

        if piece and type(piece).__name__ == "Rook" and piece.can_castle:
            return True
        
        return False
    
    def is_castling_move(self, initial_square, destination_square):
        """
        I need this method for the Board.move_piece to identify
        if it's a castling move, to be able to move the rook
        """
        dx, dy = self.dxdy(initial_square, destination_square)

        return dx == 0 and dy == 2