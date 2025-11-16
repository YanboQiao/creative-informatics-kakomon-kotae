from ast import literal_eval

import numpy as np
import pwlf

def read_data(path: str) -> list[tuple[int, int]]:
    tens = []
    with open(path, "r", encoding="utf-8") as fp:
        for line in fp:
            line = line.strip()
            if not line:
                continue
            tens.append(tuple(literal_eval(line)))
    return tens

def get_ab(tens : list[tuple[int, int]]) -> tuple[float, float]:
    a, b = 0.0, 0.0
    nagasa = len(tens)
    sumX, sumY, sumXY, sum_x_suare = 0.0, 0.0, 0.0, 0.0

    for i in range(nagasa):
        x, y = tens[i]
        sumX += x
        sumY += y
        sumXY += x * y
        sum_x_suare += x * x

    sumX_square = sumX * sumX
    BCS = nagasa * sum_x_suare - sumX_square

    if BCS == 0 :
        raise ZeroDivisionError("所有 x 相同，无法求最小二乘直线")

    a = (nagasa * sumXY - sumX * sumY) / BCS
    b = (sum_x_suare * sumY - sumXY * sumX) / BCS
    
    return (a, b)

def board_init(x: int, y: int) -> list[list[str]]:
    board = [[' ' for _ in range(2 * x + 5)] for _ in range(y + 5)]
    for i in range(len(board)):
        board[i][2] = '|'
    board[1][0] = '0'
    board[11][0] = '1'
    board[11][1] = '0'
    board[21][0] = '2'
    board[21][1] = '0'
    board[31][0] = '3'
    board[31][1] = '0'
    board[0][2] = '0'
    board[0][22] = '1'
    board[0][23] = '0'
    board[0][42] = '2'
    board[0][43] = '0'
    board[0][62] = '3'
    board[0][63] = '0'
    for i in range(2, 2 * x + 5, 1):
        board[1][i] = '-'
    board[1][2] = '+'
    return board

    

def draw_plot(board : list[list[str]], ten : list[tuple[int, int]]) -> list[list[str]]:
    for i in range(len(ten)):
        x, y = ten[i]
        board[y + 1][2 * x + 2] = '*'
    return board

def draw_line(board : list[list[str]], a : float, b: float) -> list[tuple[int, int]]:
    for i in range(2, len(board[0])):
        x = i
        y_real = a * ((i - 2) / 2) + b - 1
        y = int(round(y_real))
        if 0 <= y < len(board) and abs(y_real - y) < 0.2:
            board[y+2][x] = 'o'
    return board
    
def print_board(board: list[list[str]]) -> None:
    for row in reversed(board):
        print(''.join(row))

def get_two_line(ten: list[tuple[int, int]]) -> tuple[float, float, float, float, float]:
    """
    使用 pwlf 对输入点进行两段连续线性拟合。
    返回 (a1, b1, a2, b2, xm)
      - a1, b1: 左段直线参数 y = a1*x + b1
      - a2, b2: 右段直线参数 y = a2*x + b2
      - xm: 断点位置
    """
    # 转为 numpy 数组并按 x 排序
    pts = np.array(ten, dtype=float)
    pts = pts[np.argsort(pts[:, 0])]
    x, y = pts[:, 0], pts[:, 1]

    # 构建模型并拟合两段
    model = pwlf.PiecewiseLinFit(x, y)
    breaks = model.fit(2)  # 自动寻找一个断点（即两段）
    slopes = model.slopes  # [a1, a2]
    intercepts = model.intercepts  # [b1, b2]
    xm = breaks[1]

    return float(slopes[0]), float(intercepts[0]), float(slopes[1]), float(intercepts[1]), float(xm)
