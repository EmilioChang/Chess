from .Piece import Piece
from ..GUI import Utils

class Bishop(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)

    def piece_image(self):
        if self.is_white:
            return Utils.pieces["wb"]
        else:
            return Utils.pieces["bb"]
        
    def piece_notation(self):
        return "B"

    def move(self, board, initial_square, destination_square):
        if self.has_friendly_piece(destination_square):
            return False
        
        if not self.is_diagonal_move(initial_square, destination_square):
            return False
        
        return self.is_valid_path(board, initial_square, destination_square)
        
    def is_valid_path(self, board, initial_square, destination_square):
        step_x = 1 if destination_square.x > initial_square.x else -1
        step_y = 1 if destination_square.y > initial_square.y else -1

        x = initial_square.x + step_x
        y = initial_square.y + step_y

        while x != destination_square.x and y != destination_square.y:
            if board[x][y].piece:
                return False
            x += step_x
            y += step_y

        return True