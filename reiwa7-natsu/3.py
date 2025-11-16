from pathlib import Path
import utils

def solve_format3(data: list[int], r: int, c: int) -> list[float]:
    if len(data) % 2 != 0:
        raise ValueError("数据长度必须是 2 的倍数。")

    row_sums = [0.0 for _ in range(r)]
    total_cells = r * c
    idx = 0

    for i in range(0, len(data), 2):
        zero_num = int(data[i])
        value = float(data[i + 1])
        if zero_num < 0:
            raise ValueError("零段长度不能为负数。")
        idx += zero_num
        if idx >= total_cells:
            raise ValueError("游标超出棋盘范围。")

        row = idx // c
        row_sums[row] += value
        idx += 1

    return row_sums

def solve_case(base_dir: Path, filename: str, r: int, c: int) -> tuple[int, float]:
    data = utils.read_from_file(str(base_dir/"data"/filename))
    row_sums = solve_format3(data, r, c)
    best_row = 1
    best_sum = row_sums[0]
    for row_idx in range(1, r):
        total = row_sums[row_idx]
        if total > best_sum:
            best_sum = total
            best_row = row_idx + 1
    return best_row, best_sum

def main():
    base_dir = Path(__file__).resolve().parent
    cases = [
        ("data3a.txt", 4, 6),
        ("data3b.txt", 100, 150),
        ("data3c.txt", 10**6, 10**6),
    ]
    for filename, r, c in cases:
        print(solve_case(base_dir, filename, r, c))

if __name__ == "__main__":
    main()
