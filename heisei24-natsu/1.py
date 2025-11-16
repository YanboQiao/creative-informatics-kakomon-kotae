retsu, gyou = 9, 15

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


if __name__ == "__main__":
    board = board_init(gyou, retsu)
    output = board_to_string(board)

    with open("kotae1.txt", "w", encoding="utf-8") as f:
        f.write(output + "\n")