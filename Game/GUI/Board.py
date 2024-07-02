from .Square import Square
from ..Pieces.Rook import Rook
from ..Pieces.Knight import Knight
from ..Pieces.Bishop import Bishop
from ..Pieces.Queen import Queen
from ..Pieces.King import King
from ..Pieces.Pawn import Pawn

class Board:
    def __init__(self):
        self.board = []
        self.board_image = "Game/GUI/imgs/empty_board.png"
        self.create_board()

    def create_board(self):
        for i in range(8):
            row = []
            for j in range(8):
                row.append(Square(None, i, j))
            self.board.append(row)

        self.board[7][0] = Square(Rook(True), 7, 0)
        self.board[7][1] = Square(Knight(True), 7, 1)
        self.board[7][2] = Square(Bishop(True), 7, 2)
        self.board[7][3] = Square(Queen(True), 7, 3)
        self.board[7][4] = Square(King(True), 7, 4)
        self.board[7][5] = Square(Bishop(True), 7, 5)
        self.board[7][6] = Square(Knight(True), 7, 6)
        self.board[7][7] = Square(Rook(True), 7, 7)

        for i in range(8):
            self.board[6][i] = Square(Pawn(True), 6, i)

        self.board[0][0] = Square(Rook(False), 0, 0)
        self.board[0][1] = Square(Knight(False), 0, 1)
        self.board[0][2] = Square(Bishop(False), 0, 2)
        self.board[0][3] = Square(Queen(False), 0, 3)
        self.board[0][4] = Square(King(False), 0, 4)
        self.board[0][5] = Square(Bishop(False), 0, 5)
        self.board[0][6] = Square(Knight(False), 0, 6)
        self.board[0][7] = Square(Rook(False), 0, 7)

        for i in range(8):
            self.board[1][i] = Square(Pawn(False), 1, i)

    def set_square(self, x, y, piece):
        self.board[x][y] = Square(piece, x, y)

    def move_piece(self, start_coordenates, destination_coordenates):
        piece = self.board[start_coordenates[0]][start_coordenates[1]].piece
        initial_square = self.board[start_coordenates[0]][start_coordenates[1]]
        destination_square = self.board[destination_coordenates[0]][destination_coordenates[1]]
        valid_move = None

        if type(piece).__name__ == "NoneType":
            return False
        
        if type(piece).__name__ == "Knight":
            valid_move = piece.move(initial_square, destination_square)
        else:
            valid_move = piece.move(self.board, initial_square, destination_square)
        
        if valid_move:
            self.board[destination_coordenates[0]][destination_coordenates[1]].piece = piece
            self.board[start_coordenates[0]][start_coordenates[1]].piece = None
            return True
        
        return False