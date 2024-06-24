from abc import ABC, abstractmethod
#ABC = abstract class

class Piece(ABC):
    is_white = None

    def __init__(self, is_white) -> None:
        self.is_white = is_white

    @abstractmethod
    def move():
        pass