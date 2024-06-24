import Piece

class Bishop(Piece):
    def __init__(self, is_white) -> None:
        super().__init__(is_white)

    def move(self, board, initial_square, destination_square):
        if destination_square.piece and destination_square.piece.is_white == self.is_white:
            return False
        
        if not self.is_diagonal_move(board, initial_square, destination_square):
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

    def is_diagonal_move(self, initial_square, destination_square):
        dx = abs(initial_square.x - destination_square.x)
        dy = abs(initial_square.y - destination_square.y)

        return dx == dy