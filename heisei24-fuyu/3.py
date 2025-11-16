import utils
from pathlib import Path

board = utils.board_init(30, 30)
board = utils.draw_line(board, 0.5, 10.0)

utils.print_board(board)