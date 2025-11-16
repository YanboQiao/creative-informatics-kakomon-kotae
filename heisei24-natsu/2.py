import time

retsu, gyou = 9, 15
dx, dy = 1, 1
x, y = 5, 0

def board_init(gyou: int, retsu: int) -> list[list[str]]:
    board = [[' ' for _ in range(retsu)] for _ in range(gyou)]

    for i in range(retsu):
        board[0][i] = '_'
        board[gyou - 1][i] = '.'

    for j in range(gyou):
        board[j][0] = '|'
        board[j][retsu - 1] = '|'

    board[0][retsu // 2] = 'V'
    board[gyou - 1][retsu // 2] = 'X'

    return board

def board_to_string(board):
    return '\n'.join(''.join(row) for row in board)

def update_ichi(ichi: tuple[int, int], houhou: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    x, y = ichi[0], ichi[1]
    dx, dy = houhou[0], houhou[1]

    # 到达 C（底边）后从1 A 中央重生
    if y >= gyou - 1:
        return (retsu // 2, 0), (1, 1)

    # 侧壁 B/D 反射
    if x <= 0 or x >= retsu - 1:
        dx = -dx

    # 按45度右下移动
    x += dx
    y += dy

    return (x, y), (dx, dy)

def print_board(board: list[list[str]]) -> None:
    # 控制台打印
    print("\033[H\033[J", end="")  # 清屏
    print(board_to_string(board))

def main():
    global x, y, dx, dy

    base = board_init(gyou, retsu)
    board = [row[:] for row in base]

    # 初始目标
    x, y = retsu // 2, 0
    dx, dy = 1, 1

    while True:
        # 放置目标（注意[y][x]）
        board[y][x] = 'O'
        print_board(board)
        # 恢复该位置字符
        board[y][x] = base[y][x]

        # 计算下一步并回写全局位置与方向
        (x, y), (dx, dy) = update_ichi((x, y), (dx, dy))

        time.sleep(0.5)

if __name__ == '__main__':
    main()
