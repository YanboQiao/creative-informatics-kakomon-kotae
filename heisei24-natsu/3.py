import select
import sys
import time

def board_init(gyou: int, retsu: int) -> list[list[str]]:
    board = [[' ' for _ in range(retsu)] for _ in range(gyou)]

    for i in range(retsu):
        board[0][i] = '-'
        board[gyou - 1][i] = '.'

    for j in range(gyou):
        board[j][0] = '|'
        board[j][retsu - 1] = '|'

    board[0][retsu // 2] = 'V'
    board[gyou - 1][retsu // 2] = 'G'

    return board

def board_to_string(board):
    return '\n'.join(''.join(row) for row in board)

def update_mokuhyou_ichi(ichi: tuple[int, int], houhou: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    x, y = ichi[0], ichi[1]
    dx, dy = houhou[0], houhou[1]
    if y >= gyou - 1:
        return (retsu // 2, 0), (1, 1)
    
    if x <= 0 or x >= retsu - 1:
        dx = -dx

    x += dx
    y += dy

    return (x, y), (dx, dy)

def update_bullet_ichis(ichis: list[tuple[int, int]]) -> list[tuple[int, int]]:
    while ichis and ichis[0][1] <= 1:
        ichis.pop(0)  # 删除第一个元素
    return [(x, y - 1) for x, y in ichis if y > 1]


def collision_detection(bullet_ichis: list[tuple[int, int]], mokuhyou: tuple[int, int]) -> tuple[list[tuple[int, int]], bool]:
    hits = [ich for ich in bullet_ichis if ich == mokuhyou]
    if hits:
        bullet_ichis[:] = [ich for ich in bullet_ichis if ich != mokuhyou]
    
    return bullet_ichis, bool(hits)

def draw_board(base: list[list[str]], bullet_ichis: list[tuple[int, int]], mokuhyou_ichi: tuple[int, int]) -> list[list[str]]:
    board = [row[:] for row in base]

    mx, my = mokuhyou_ichi
    board[my][mx] = 'O'

    for ix, iy in bullet_ichis:
        board[iy][ix] = '•'

    return board

def print_board(board: list[list[str]]) -> None:
    # 控制台打印
    print("\033[H\033[J", end="")  # 清屏
    print(board_to_string(board))
    print(f"score: {score}")

def main():
    global retsu, gyou, dx, dy, x, y, score
    retsu, gyou = 9, 15
    dx, dy = 1, 1
    x, y = 5, 0
    score = 0

    base = board_init(gyou, retsu)
    board = [row[:] for row in base]
    bullet_ichis: list[tuple[int, int]] = []
    gun_position = (retsu // 2, gyou - 2)

    while True:
        mokuhyou_ichi = (x, y)
        bullet_ichis = update_bullet_ichis(bullet_ichis)
        bullet_ichis, hit = collision_detection(bullet_ichis, mokuhyou_ichi)
        if hit:
            score += 1
            x, y = retsu // 2, 0
            dx, dy = 1, 1
            mokuhyou_ichi = (x, y)

        try:
            ready, _, _ = select.select([sys.stdin], [], [], 0)
        except (OSError, ValueError):
            ready = []
        if ready:
            command = sys.stdin.readline().strip().lower()
            if 'i' in command:
                bullet_ichis.append(gun_position)

        board = draw_board(base, bullet_ichis, mokuhyou_ichi)
        print_board(board)

        # 计算下一步并回写全局位置与方向
        (x, y), (dx, dy) = update_mokuhyou_ichi((x, y), (dx, dy))

        time.sleep(1.0)

if __name__ == '__main__':
    main()
