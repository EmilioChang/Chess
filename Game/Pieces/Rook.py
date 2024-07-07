from .Piece import Piece
from ..GUI import Utils

class Rook(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)
        self.can_castle = True

    def piece_image(self):
        if self.is_white:
            return Utils.pieces["wr"]
        else:
            return Utils.pieces["br"]
        
    def piece_notation():
        return "R"

    def move(self, board, initial_square, destination_square):
        self.can_castle = False
        return not self.has_friendly_piece(destination_square) and self.is_valid_path(board, initial_square, destination_square)

    def is_valid_path(self, board, initial_square, destination_square):
        if self.is_horizontal_move(initial_square, destination_square):
            row = initial_square.x
            min_col = min(initial_square.y, destination_square.y) + 1
            max_col = max(initial_square.y, destination_square.y)

            for col in range(min_col, max_col):
                if board[row][col].piece is not None:
                    return False

            return True

        if self.is_straight_move(initial_square, destination_square):
            col = initial_square.y
            min_row = min(initial_square.x, destination_square.x) + 1
            max_row = max(initial_square.x, destination_square.x)

            for row in range(min_row, max_row):
                if board[row][col].piece is not None:
                    return False

            return True

        return False