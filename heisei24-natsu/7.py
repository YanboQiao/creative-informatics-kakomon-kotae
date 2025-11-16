import os
import random
import select
import sys
import time
import termios
import tty

def choose_randon_point(retsu: int)-> int:
    return random.randint(1, retsu - 2)

def board_init(gyou: int, retsu: int) -> list[list[str]]:
    board = [[' ' for _ in range(retsu)] for _ in range(gyou)]
    for i in range(retsu):
        board[0][i] = '-'
        board[-1][i] = '.'

    for j in range(gyou):
        board[j][0] = '|'
        board[j][-1] = '|'
    
    return board

def board_to_string(board : list[list[str]]):
    return '\n'.join(''.join(row) for row in board)

def update_mokuhyou_ichi(ichi: tuple[int, int], houhou: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    global rdx
    (x, y) = ichi


def main():
    global retsu, gyou, dx, dy, x, y, score, rdx
    retsu, gyou = 9, 15
    dx, dy = 1, 1
    rdx = choose_randon_point(retsu)
    x, y = rdx, 0
    score = 0

    base = board_init(retsu, gyou)
    board = [row[:] for row in base]
    bullet_ichis = list[tuple[int, int]]
    gun_position = [retsu // 2, gyou - 1]
    input_buffer = ""
    