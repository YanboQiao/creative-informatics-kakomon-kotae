from collections import defaultdict
from pathlib import Path

import utils


def triple_tuple(data: list[int]) -> list[tuple[int, int, int]]:
    if len(data) % 3 != 0:
        raise ValueError("数据长度必须是 3 的倍数。")

    triples: list[tuple[int, int, int]] = []
    for idx in range(0, len(data), 3):
        row, col, value = data[idx : idx + 3]
        triples.append((row, col, value))
    return triples


def find_max_row_sum(triples: list[tuple[int, int, int]], r: int, c: int) -> tuple[int, int]:
    row_sums: defaultdict[int, int] = defaultdict(int)
    for row, col, value in triples:
        if not (1 <= row <= r):
            raise ValueError(f"行号 {row} 超出范围 1..{r}")
        if not (1 <= col <= c):
            raise ValueError(f"列号 {col} 超出范围 1..{c}")
        row_sums[row] += value

    best_row = 1
    best_sum = row_sums.get(1, 0)
    for row_idx in range(2, r + 1):
        total = row_sums.get(row_idx, 0)
        if total > best_sum:
            best_row = row_idx
            best_sum = total
    return best_row, best_sum


def solve_case(base_dir: Path, filename: str, r: int, c: int) -> tuple[int, int]:
    data = utils.read_from_file(str(base_dir/"data"/filename))
    triples = triple_tuple(data)
    return find_max_row_sum(triples, r, c)


def main():
    base_dir = Path(__file__).resolve().parent
    cases = [
        ("data2a.txt", 6, 4),
        ("data2b.txt", 100, 150),
        ("data2c.txt", 10**6, 10**6),
    ]

    for filename, r, c in cases:
        print(solve_case(base_dir, filename, r, c))

if __name__ == "__main__":
    main()