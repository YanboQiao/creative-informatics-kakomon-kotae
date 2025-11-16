import utils
from pathlib import Path

board = utils.board_init(30, 30)
tens = utils.read_data(Path(__file__).with_name("data2.txt"))

a, b = utils.get_ab(tens)
print(a, b)
board = utils.draw_line(board, a, b)
board = utils.draw_plot(board, tens)

utils.print_board(board)