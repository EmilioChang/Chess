class Move():
    def __init__(self, initial_square, destination_square):
        self.initial_square = initial_square
        self.destination_square = destination_square
        self.notation = None

        if destination_square.piece:
            if type(destination_square.piece).__name__ == "Pawn":
                self.notation = initial_square.name[0] + "x" + destination_square.name
            else:
                self.notation = initial_square.piece.piece_notation() + "x" + destination_square.name
        else:
            self.notation = initial_square.piece.piece_notation() + destination_square.name
