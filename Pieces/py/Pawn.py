import Piece

class Pawn(Piece):
    made_first_move = False

    def __init__(self, is_white):
        super().__init__(is_white)

    def move(self, board, initial_square, destination_square):
        dx = abs(initial_square.x - destination_square.x)
        status = None

        if destination_square.piece and destination_square.piece.is_white == self.is_white:
            status = False
        elif dx > 2:
            status = False
        elif dx == 2:
            stauts = self.valid_double_move(board, initial_square, destination_square)
        else:
            status = self.valid_forward_move(initial_square, destination_square)
        

        self.made_first_move = True
        return status
    
    def valid_double_move(self, board, initial_square, destination_square):
        if self.made_first_move:
            return False
        
        # Check if the pawn is moving diagonally
        if initial_square.y != destination_square.y:
            return False
        
        # Check if there are pieces on the way
        direction = -1 if self.is_white else 1

        if board[initial_square.x + direction][initial_square.y].piece:
            return False
        if destination_square.piece:
            return False
        
        return True
    
    def valid_forward_move(self, initial_square, destination_square):
        if initial_square.y != destination_square.y:
            return False
        
        if abs(initial_square.x - destination_square.x) != 1:
            return False
        
        return True
    
    def take(self):
        # TODO
        pass

    def en_passant(self):
        # TODO
        pass