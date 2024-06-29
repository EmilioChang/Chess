import pygame
from .Board import Board
from .Utils import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((width_of_window, height_of_window))
        pygame.display.set_caption('Chess')
        self.board = Board()
        self.background_image = pygame.image.load(self.board.board_image)
        self.moving_piece = None
        self.start_coordenates = None
        self.destination_coordenates = None
        self.whites_turn = True

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
                    self.start_coordenates = (row, col)

                    self.moving_piece = self.board.get_square(row, col).get_piece()

                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    row = int((y - edges_offset) // tile_size_height)
                    col = int((x - edges_offset) // tile_size_width)
                    self.destination_coordenates = (row, col)

                    if self.moving_piece and self.moving_piece.is_white == self.whites_turn:
                        if self.board.move_piece(self.start_coordenates, self.destination_coordenates):
                            self.whites_turn = not self.whites_turn

            self.print_board()

        pygame.quit()

    def print_board(self):
        self.screen.blit(self.background_image, (0, 0))
        for row in range(8):
                for col in range(8):
                    piece = self.board.get_square(row, col).get_piece()
                    if piece:
                        piece_image = pygame.image.load(piece.piece_image())
                        piece_width, piece_height = piece_image.get_size()
                        x = col * tile_size_width + edges_offset + (tile_size_width - piece_width) / 2
                        y = row * tile_size_height + edges_offset + (tile_size_height - piece_height) / 2
                        self.screen.blit(piece_image, (x, y))
        pygame.display.update()

Game().init_game()