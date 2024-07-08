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
                # cast to char
                row.append(Square(f"{chr(j + 97)}{8-i}", None, i, j)) # chr(65) = A
            self.board.append(row)

        self.board[7][0] = Square("a1", Rook(True), 7, 0)
        self.board[7][1] = Square("b1", Knight(True), 7, 1)
        self.board[7][2] = Square("c1", Bishop(True), 7, 2)
        self.board[7][3] = Square("d1", Queen(True), 7, 3)
        self.board[7][4] = Square("e1", King(True), 7, 4)
        self.board[7][5] = Square("f1", Bishop(True), 7, 5)
        self.board[7][6] = Square("g1", Knight(True), 7, 6)
        self.board[7][7] = Square("h1", Rook(True), 7, 7)

        for i in range(8):
            self.board[6][i] = Square(f"{chr(i+97)}2", Pawn(True), 6, i)

        self.board[0][0] = Square("a8", Rook(False), 0, 0)
        self.board[0][1] = Square("b8", Knight(False), 0, 1)
        self.board[0][2] = Square("c8", Bishop(False), 0, 2)
        self.board[0][3] = Square("d8", Queen(False), 0, 3)
        self.board[0][4] = Square("e8", King(False), 0, 4)
        self.board[0][5] = Square("f8", Bishop(False), 0, 5)
        self.board[0][6] = Square("g8", Knight(False), 0, 6)
        self.board[0][7] = Square("h8", Rook(False), 0, 7)

        for i in range(8):
            self.board[1][i] = Square(f"{chr(i+97)}7", Pawn(False), 1, i)

    def move_piece(self, initial_square, destination_square):
        piece = self.board[initial_square.x][initial_square.y].piece
        valid_move = None
        is_castling_move = None

        if type(piece).__name__ == "NoneType":
            return False
        
        if type(piece).__name__ == "Knight":
            valid_move = piece.move(initial_square, destination_square)
        else:
            if type(piece).__name__ == "King" and piece.is_castling_move(initial_square, destination_square):
                is_castling_move = True
            valid_move = piece.move(self.board, initial_square, destination_square)
        
        if valid_move:
            if is_castling_move:
                x = initial_square.x
                y = initial_square.y
                y_castling_direction = (1 if initial_square.y < destination_square.y else -1) + y
                y_rook_position = (3 if initial_square.y < destination_square.y else -4) + y

                # Move the Rook beside the King
                rook = self.board[x][y_rook_position].piece
                self.board[initial_square.x][y_castling_direction].piece = rook

                # Remove the Rook from its initial square
                self.board[initial_square.x][y_rook_position].piece = None

                # King is moved on the next 2 lines

            self.board[destination_square.x][destination_square.y].piece = piece
            self.board[initial_square.x][initial_square.y].piece = None

            return True
        
        return False