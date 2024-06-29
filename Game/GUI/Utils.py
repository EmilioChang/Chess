# https://www.remove.bg/
#https://greenchess.net/info.php?item=downloads

edges_offset = 28
width_of_window = 832 # Same as image size
height_of_window = 832 # Same as image size
tile_size_height = (height_of_window - 2 * edges_offset) / 8
tile_size_width = (width_of_window - 2 * edges_offset) / 8

empty_board = "Game/GUI/imgs/empty_board.png"

black_pawn = "Game/GUI/imgs/black_pawn.png"
black_rook = "Game/GUI/imgs/black_rook.png"
black_knight = "Game/GUI/imgs/black_knight.png"
black_bishop = "Game/GUI/imgs/black_bishop.png"
black_queen = "Game/GUI/imgs/black_queen.png"
black_king = "Game/GUI/imgs/black_king.png"

white_pawn = "Game/GUI/imgs/white_pawn.png"
white_rook = "Game/GUI/imgs/white_rook.png"
white_knight = "Game/GUI/imgs/white_knight.png"
white_bishop = "Game/GUI/imgs/white_bishop.png"
white_queen = "Game/GUI/imgs/white_queen.png"
white_king = "Game/GUI/imgs/white_king.png"

pieces = {
    "bp": black_pawn,
    "br": black_rook,
    "bn": black_knight,
    "bb": black_bishop,
    "bq": black_queen,
    "bk": black_king,
    "wp": white_pawn,
    "wr": white_rook,
    "wn": white_knight,
    "wb": white_bishop,
    "wq": white_queen,
    "wk": white_king
}