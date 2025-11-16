import utils
from pathlib import Path

data = utils.read_data(Path(__file__).with_name("data2.txt"))
a1, a2, a3, a4, a5 = utils.get_two_line(data)
print(a1, a2, a3, a4, a5)