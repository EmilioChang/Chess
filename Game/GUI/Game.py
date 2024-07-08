import pygame
import copy
from .Board import Board
from .Utils import *
from .Player import Player
from .Move import Move

class Game:
    def __init__(self):
        self.played_moves = []
        self.screen = pygame.display.set_mode((width_of_window, height_of_window))
        pygame.display.set_caption('Chess')
        self.board = Board()
        self.background_image = pygame.image.load(self.board.board_image)

        self.moving_piece = None
        self.initial_square = None
        self.destination_square = None
        self.whites_turn = True
        self.white_player = Player("white")
        self.black_player = Player("black")

        self.moves = []
        self.current_move = []

    def init_game(self):
        pygame.init()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    row = int((y - edges_offset) // tile_size_height)
                    col = int((x - edges_offset) // tile_size_width)
                    self.initial_square = self.board.board[row][col]

                    self.moving_piece = self.board.board[row][col].piece

                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    row = int((y - edges_offset) // tile_size_height)
                    col = int((x - edges_offset) // tile_size_width)
                    self.destination_square = self.board.board[row][col]

                    if self.moving_piece and self.moving_piece.is_white == self.whites_turn:
                        # Once the nedt `if`` is ran, the piece (s) is (are) moved from the squares
                        # so I need a reference to the squares before the moves are made

                        initial_square_copy = copy.deepcopy(self.initial_square)
                        destination_square_copy = copy.deepcopy(self.destination_square)

                        if self.board.move_piece(self.initial_square, self.destination_square):
                            if self.whites_turn:
                                self.current_move.append(Move(initial_square_copy, destination_square_copy).notation)
                            else:
                                self.current_move.append(Move(initial_square_copy, destination_square_copy).notation)
                                self.moves.append(self.current_move)
                                self.current_move = []
                                print(self.moves[-1])

                            self.whites_turn = not self.whites_turn


            self.print_board()

        pygame.quit()

    def print_board(self):
        self.screen.blit(self.background_image, (0, 0))
        for row in range(8):
                for col in range(8):
                    piece = self.board.board[row][col].piece
                    if piece:
                        piece_image = pygame.image.load(piece.piece_image())
                        piece_width, piece_height = piece_image.get_size()
                        x = col * tile_size_width + edges_offset + (tile_size_width - piece_width) / 2
                        y = row * tile_size_height + edges_offset + (tile_size_height - piece_height) / 2
                        self.screen.blit(piece_image, (x, y))
        pygame.display.update()

    def print_moves(self):
        print

Game().init_game()