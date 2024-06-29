from abc import ABC, abstractmethod
#ABC = abstract class

class Piece(ABC):
    def __init__(self, is_white) -> None:
        self.is_white = is_white

    @abstractmethod
    def piece_image():
        pass

    @abstractmethod
    def move():
        pass

