import utils

tens = utils.read_data("heisei24-fuyu/data1.txt")

x, y = 0, 0

for i in range(len(tens)):
    nx, ny = tens[i]
    if ny > y:
        x = nx
        y = ny

print(x, y)