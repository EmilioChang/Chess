from abc import ABC, abstractmethod
#ABC = abstract class

class Piece(ABC):
    def __init__(self, is_white) -> None:
        self.is_white = is_white

    @abstractmethod
    def piece_image():
        pass

    @abstractmethod
    def piece_notation():
        pass

    @abstractmethod
    def move():
        pass

    def dxdy(self, initial_square, destination_square):
        return abs(initial_square.x - destination_square.x), abs(initial_square.y - destination_square.y)

    def has_friendly_piece(self, destination_square):
        if destination_square.piece and destination_square.piece.is_white == self.is_white:
            return True
        
        return False

    def is_diagonal_move(self, initial_square, destination_square):
        dx = abs(initial_square.x - destination_square.x)
        dy = abs(initial_square.y - destination_square.y)

        return dx == dy
    
    def is_horizontal_move(self, initial_square, destination_square):
        return initial_square.x == destination_square.x

    def is_straight_move(self, initial_square, destination_square):
        return initial_square.y == destination_square.y
