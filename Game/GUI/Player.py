class Player:
    def __init__(self, color):
        self.color = color
        self.is_white = (color == "white")
        self.score = 0

    def move(self, board, initial_square, destination_square):
        return board.move_piece(initial_square, destination_square)