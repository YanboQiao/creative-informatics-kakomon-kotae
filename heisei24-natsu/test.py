RETSU = 9
GYOU = 15

GUN_X = RETSU // 2
GUN_Y = GYOU - 1
BULLET_START = (GUN_X, GUN_Y - 1)
TARGET_START = (RETSU // 2, 0)
DEFAULT_DIRECTION = (1, 1)
BULLET_CHAR = '•'
TARGET_CHAR = 'O'


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


def board_to_string(board: list[list[str]]) -> str:
    return '\n'.join(''.join(row) for row in board)


def print_board(board: list[list[str]], score: int) -> None:
    print("\033[H\033[J", end="")
    print(board_to_string(board))
    print(f"Score: {score}")


def advance_target(position: tuple[int, int], direction: tuple[int, int]) -> tuple[tuple[int, int] | None, tuple[int, int], bool]:
    x, y = position
    dx, dy = direction

    if x <= 0 or x >= RETSU - 1:
        dx = -dx

    x += dx
    y += dy

    if y >= GYOU - 1:
        return None, (dx, dy), True

    return (x, y), (dx, dy), False


def advance_bullets(
    bullets: list[tuple[int, int]],
    target_pos: tuple[int, int] | None,
    previous_target: tuple[int, int] | None,
) -> tuple[list[tuple[int, int]], bool]:
    updated: list[tuple[int, int]] = []
    hit_target = False

    for x, y in bullets:
        new_y = y - 1

        if target_pos is not None and (x, new_y) == target_pos:
            hit_target = True
            continue

        if (
            target_pos is not None
            and previous_target is not None
            and (x, y) == target_pos
            and (x, new_y) == previous_target
        ):
            hit_target = True
            continue

        if new_y <= 0:
            continue

        updated.append((x, new_y))

    return updated, hit_target


def draw_board(base: list[list[str]], target_pos: tuple[int, int] | None, bullets: list[tuple[int, int]]) -> list[list[str]]:
    board = [row[:] for row in base]

    if target_pos is not None:
        tx, ty = target_pos
        board[ty][tx] = TARGET_CHAR

    for bx, by in bullets:
        if 0 < by < GYOU - 1:
            board[by][bx] = BULLET_CHAR

    return board


def main() -> None:
    base_board = board_init(GYOU, RETSU)
    target_pos: tuple[int, int] | None = None
    target_dir = DEFAULT_DIRECTION
    bullets: list[tuple[int, int]] = []
    score = 0

    try:
        while True:
            if target_pos is None:
                target_pos = TARGET_START
                target_dir = DEFAULT_DIRECTION

            board = draw_board(base_board, target_pos, bullets)
            print_board(board, score)

            command = input("输入 i 发射，k 更新（其他键忽略）：").strip().lower()
            if command == 'i':
                bullets.append(BULLET_START)

            previous_target = target_pos
            reached_bottom = False
            if target_pos is not None:
                target_pos, target_dir, reached_bottom = advance_target(target_pos, target_dir)
                if reached_bottom:
                    target_pos = None

            bullets, hit = advance_bullets(bullets, target_pos, previous_target)
            if hit:
                score += 1
                target_pos = None
                target_dir = DEFAULT_DIRECTION
    except KeyboardInterrupt:
        print("\n游戏结束")


if __name__ == '__main__':
    main()
