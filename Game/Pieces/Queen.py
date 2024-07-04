from .Piece import Piece
from ..GUI import Utils

class Queen(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)

    def piece_image(self):
        if self.is_white:
            return Utils.pieces["wq"]
        else:
            return Utils.pieces["bq"]
        
    def piece_notation():
        return "Q"

    def move(self, board, initial_square, destination_square):       
        return not self.has_friendly_piece(destination_square) and self.is_valid_path(board, initial_square, destination_square)

    def is_valid_path(self, board, initial_square, destination_square):
        step_x = 1 if destination_square.x > initial_square.x else -1
        step_y = 1 if destination_square.y > initial_square.y else -1

        x = initial_square.x + step_x
        y = initial_square.y + step_y

        if self.is_horizontal_move(initial_square, destination_square):
            row = initial_square.x
            while y != destination_square.y:
                if board[row][y].piece:
                    return False  # There is a piece blocking the path
                y += step_y
            return True

        if self.is_straight_move(initial_square, destination_square):
            col = initial_square.y
            while x != destination_square.x:
                if board[x][col].piece:
                    return False  # There is a piece blocking the path
                x += step_x
            return True

        if self.is_diagonal_move(initial_square, destination_square):
            while x != destination_square.x and y != destination_square.y:
                if board[x][y].piece:
                    return False  # There is a piece blocking the path
                x += step_x
                y += step_y
            return True

        return False
