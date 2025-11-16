import utils
from pathlib import Path

board = utils.board_init(30, 30)
tens = utils.read_data(Path(__file__).with_name("data1.txt"))

board = utils.draw_plot(board, tens)

utils.print_board(board)