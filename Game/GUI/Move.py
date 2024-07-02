class Move():
    def __init__(self):
        self.initial_square = None
        self.destination_square = None
        self.notation = None

    def translate_move_to_notation(self, initial_square, destination_square):
        piece1 = initial_square.piece
        piece2 = destination_square.piece

        
