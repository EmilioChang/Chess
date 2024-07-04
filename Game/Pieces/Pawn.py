from .Piece import Piece
from ..GUI import Utils

class Pawn(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)
        self.made_first_move = False

    def piece_image(self):
        if self.is_white:
            return Utils.pieces["wp"]
        else:
            return Utils.pieces["bp"]
        
    def piece_notation():
        pass

    def move(self, board, initial_square, destination_square):
        if self.has_friendly_piece(destination_square):
            return False
        
        dx, dy = self.dxdy(initial_square, destination_square)
        status = None

        if dx > 2:
            status = False
        elif dx == 1 and dy == 0:
            status = self.valid_forward_move(initial_square, destination_square)
        elif dx == 2:
            status = self.valid_double_move(board, initial_square, destination_square)
        elif self.is_diagonal_move(initial_square, destination_square):
            status = self.take(board, initial_square, destination_square)
        else:
            status = False
        
        self.made_first_move = True
        return status
    
    def valid_double_move(self, board, initial_square, destination_square):
        if self.made_first_move:
            return False
        
        # Check if the pawn is moving diagonally
        if self.is_diagonal_move(initial_square, destination_square):
            return False
        
        # Check if there are pieces on the way
        direction = -1 if self.is_white else 1

        if board[initial_square.x + direction][initial_square.y].piece:
            return False
        if destination_square.piece:
            return False
        
        return True
    
    def valid_forward_move(self, initial_square, destination_square):
        if destination_square.piece:
            return False
        
        if self.is_diagonal_move(initial_square, destination_square):
            return False
        
        if abs(initial_square.x - destination_square.x) != 1:
            return False
        
        return True
    
    def take(self, board, initial_square, destination_square):
        # Check if moving diagonally or not
        if not self.is_diagonal_move(initial_square, destination_square):
            return False
        
        # Check if there are pieces on the way
        direction = -1 if self.is_white else 1
        
        if direction == -1:
            if initial_square.x < destination_square.x:
                return False
            
        else:
            if initial_square.x > destination_square.x:
                return False

        # Check if there's a piece on the destination square
        if not destination_square.piece:
            return False
        
        else:
            if destination_square.piece.is_white == self.is_white:
                return False

        return True

    def en_passant(self):
        # TODO
        pass