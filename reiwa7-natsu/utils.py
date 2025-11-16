from pathlib import Path

def find_biggest_gyou(board: list[list[float]], r: int, c: int) -> tuple[int, float]:
    best_row = 1
    best_sum = float("-inf")
    for i in range(r):
        current_sum = sum(board[i][j] for j in range(c))
        if current_sum > best_sum:
            best_sum = current_sum
            best_row = i + 1  # 题目要求行号从 1 开始
    return best_row, best_sum

def read_from_file(path: str) -> list[int]:
    """读取以逗号分隔的整数序列文件并返回整数列表。"""
    content = Path(path).read_text(encoding="utf-8").strip()
    if not content:
        return []

    tokens = (part.strip() for part in content.replace("\n", "").replace("\r", "").split(","))
    return [int(token) for token in tokens if token]

def board_init(r: int, c: int) -> list[list[float]]:
    board = [[0.0 for _ in range(c)] for _ in range(r)]
    return board