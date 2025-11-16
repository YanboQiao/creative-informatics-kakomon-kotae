from pathlib import Path

import utils


def main():
    # 确立相对路径的base path，需要背
    base_dir = Path(__file__).resolve().parent

    data = utils.read_from_file(str(base_dir / 'data1a.txt'))
    r = 6
    c = 4
    board = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            board[i][j] = data[i * c + j]
    
    saidaiGyou = utils.find_biggest_gyou(board, r, c)
    print(saidaiGyou)
    
    # 第二小问
    data = utils.read_from_file(str(base_dir / 'data1b.txt'))
    r = 100
    c = 150
    board = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            board[i][j] = data[i * c + j]
    
    saidaiGyou = utils.find_biggest_gyou(board, r, c)
    print(saidaiGyou)

if __name__ == "__main__":
    main()