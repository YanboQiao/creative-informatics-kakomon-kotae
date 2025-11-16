from __future__ import annotations

import argparse
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from collections import defaultdict

VALUE_CYCLE = [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9]
MEDIUM_MATRIX_SEED = 20240712


@dataclass(frozen=True)
class SparseEntry:
    row: int
    col: int
    value: int


@dataclass
class SparseMatrix:
    rows: int
    cols: int
    entries: list[SparseEntry]

    def __post_init__(self) -> None:
        if self.rows <= 0 or self.cols <= 0:
            raise ValueError("矩阵规模必须为正整数")
        if len(self.entries) > 10**6:
            raise ValueError("非零元素超过 10^6")

        row_counts: dict[int, int] = defaultdict(int)
        col_counts: dict[int, int] = defaultdict(int)
        seen_positions: set[tuple[int, int]] = set()

        for entry in self.entries:
            if not (-9 <= entry.value <= 9) or entry.value == 0:
                raise ValueError("条目取值必须在 [-9, 9] 且非零")
            if not (1 <= entry.row <= self.rows):
                raise ValueError("行号越界")
            if not (1 <= entry.col <= self.cols):
                raise ValueError("列号越界")

            key = (entry.row, entry.col)
            if key in seen_positions:
                raise ValueError("同一位置出现多次非零")
            seen_positions.add(key)

            row_counts[entry.row] += 1
            col_counts[entry.col] += 1
            if row_counts[entry.row] > 10 or col_counts[entry.col] > 10:
                raise ValueError("某行或某列的非零元素超过 10 个")

    def _sorted_entries(self) -> list[SparseEntry]:
        return sorted(self.entries, key=lambda entry: (entry.row, entry.col))

    def to_format2(self) -> list[int]:
        sequence: list[int] = []
        for entry in self._sorted_entries():
            sequence.extend([entry.row, entry.col, entry.value])
        return sequence

    def to_format3(self) -> list[int]:
        sequence: list[int] = []
        prev_index = -1
        for entry in self._sorted_entries():
            index = (entry.row - 1) * self.cols + (entry.col - 1)
            zeros = index - prev_index - 1
            sequence.extend([zeros, entry.value])
            prev_index = index
        return sequence


@dataclass
class DenseMatrix:
    data: list[list[int]]

    def __post_init__(self) -> None:
        if not self.data or not self.data[0]:
            raise ValueError("空矩阵无效")
        width = len(self.data[0])
        col_counts = [0] * width
        for row in self.data:
            if len(row) != width:
                raise ValueError("矩阵必须是规则的长方形")
            row_non_zero = 0
            for j, value in enumerate(row):
                if not (-9 <= value <= 9):
                    raise ValueError("元素取值必须在 [-9, 9]")
                if value:
                    row_non_zero += 1
                    col_counts[j] += 1
            if row_non_zero > 10:
                raise ValueError("某行的非零元素超过 10 个")
        if any(count > 10 for count in col_counts):
            raise ValueError("某列的非零元素超过 10 个")

    @property
    def rows(self) -> int:
        return len(self.data)

    @property
    def cols(self) -> int:
        return len(self.data[0]) if self.data else 0

    def to_format1(self) -> list[int]:
        return [value for row in self.data for value in row]

    def to_sparse(self) -> SparseMatrix:
        entries: list[SparseEntry] = []
        for i, row in enumerate(self.data, start=1):
            for j, value in enumerate(row, start=1):
                if value:
                    entries.append(SparseEntry(i, j, value))
        return SparseMatrix(self.rows, self.cols, entries)


def write_sequence(path: Path, sequence: Iterable[int]) -> None:
    values = list(sequence)
    text = ",".join(str(value) for value in values)
    if text:
        text += "\n"
    path.write_text(text, encoding="utf-8")


def build_small_dense_matrix() -> DenseMatrix:
    data = [
        [5, 0, -1, 0],
        [0, 4, 0, -3],
        [2, 0, 0, 1],
        [0, 0, 0, 0],
        [-2, 0, 3, 0],
        [0, -4, 0, 2],
    ]
    return DenseMatrix(data)


def build_medium_dense_matrix(rows: int = 100, cols: int = 150, per_row: int = 4) -> DenseMatrix:
    rng = random.Random(MEDIUM_MATRIX_SEED)
    data = [[0 for _ in range(cols)] for _ in range(rows)]
    col_counts = [0] * cols
    column_indices = list(range(cols))
    allowed_values = [-9, -8, -6, -5, -3, -2, -1, 1, 2, 3, 4, 5, 6, 8, 9]

    for row in range(rows):
        rng.shuffle(column_indices)
        filled = 0
        for col in column_indices:
            if col_counts[col] >= 10:
                continue
            value = allowed_values[rng.randrange(len(allowed_values))]
            data[row][col] = value
            col_counts[col] += 1
            filled += 1
            if filled >= per_row:
                break
        if filled < per_row:
            raise RuntimeError("列容量不足，无法放置指定数量的非零元素")

    return DenseMatrix(data)


def build_sparse_from_cross(
    rows: int,
    cols: int,
    row_positions: list[int],
    col_positions: list[int],
    offset: int = 0,
) -> SparseMatrix:
    sorted_rows = sorted(row_positions)
    sorted_cols = sorted(col_positions)
    entries: list[SparseEntry] = []
    value_index = 0
    for row in sorted_rows:
        for col in sorted_cols:
            value = VALUE_CYCLE[(value_index + offset) % len(VALUE_CYCLE)]
            entries.append(SparseEntry(row, col, value))
            value_index += 1
    return SparseMatrix(rows, cols, entries)


def build_sparse_data2c() -> SparseMatrix:
    rows = cols = 1_000_000
    row_positions = [1, 160_001, 320_001, 480_001, 640_001, 800_001]
    col_positions = [5, 9_005, 45_005, 120_005, 250_005]
    return build_sparse_from_cross(rows, cols, row_positions, col_positions, offset=1)


def build_sparse_data3a() -> SparseMatrix:
    matrix = DenseMatrix(
        [
            [0, -3, 0, 0, 7, 0],
            [4, 0, 0, -2, 0, 0],
            [0, 5, 0, 0, 0, -1],
            [0, 0, 6, 0, 0, 0],
        ]
    )
    return matrix.to_sparse()


def build_sparse_data3c() -> SparseMatrix:
    rows = cols = 1_000_000
    row_positions = [12, 200_012, 400_012, 600_012, 800_012, 900_012, 980_012]
    col_positions = [3, 10_003, 30_003, 70_003, 120_003, 170_003]
    return build_sparse_from_cross(rows, cols, row_positions, col_positions, offset=5)


def build_sparse_data4a() -> SparseMatrix:
    matrix = DenseMatrix(
        [
            [3, -1, 0, 2],
            [0, 4, -3, 0],
        ]
    )
    return matrix.to_sparse()


def build_sparse_data4b() -> SparseMatrix:
    matrix = DenseMatrix(
        [
            [0, 5, 0],
            [2, 0, -2],
            [-1, 0, 4],
            [0, -3, 1],
        ]
    )
    return matrix.to_sparse()


def build_sparse_data4c() -> SparseMatrix:
    rows = cols = 1_000_000
    row_positions = [2, 4_003, 12_007, 240_000, 490_000, 700_000, 820_000, 990_000]
    col_positions = [5, 700, 1_600, 32_000, 125_000, 500_000]
    return build_sparse_from_cross(rows, cols, row_positions, col_positions, offset=2)


def build_sparse_data4d() -> SparseMatrix:
    rows = cols = 1_000_000
    row_positions = [100, 1_500, 8_000, 20_000, 300_000, 550_000, 870_000]
    col_positions = [10, 6_000, 18_000, 47_000, 90_000, 250_000, 640_000]
    return build_sparse_from_cross(rows, cols, row_positions, col_positions, offset=4)


def build_sparse_data4e() -> SparseMatrix:
    rows = cols = 1_000_000
    row_positions = [25, 1_025, 100_025, 200_025, 300_025, 400_025, 500_025, 600_025, 700_025, 850_025]
    col_positions = [1, 11, 101, 1_001, 10_001, 20_001, 50_001, 70_001, 90_001]
    return build_sparse_from_cross(rows, cols, row_positions, col_positions, offset=1)


def build_sparse_data4f() -> SparseMatrix:
    rows = cols = 1_000_000
    row_positions = [500, 4_000, 16_000, 64_000, 125_000, 255_000, 400_000, 755_000, 990_000]
    col_positions = [3, 903, 2_903, 5_903, 10_903, 50_903, 100_903, 200_903, 400_903, 800_903]
    return build_sparse_from_cross(rows, cols, row_positions, col_positions, offset=7)


def build_sparse_data5a() -> SparseMatrix:
    matrix = DenseMatrix(
        [
            [0, 0, 1, 0, -1, 0],
            [2, -2, 0, 0, 0, 0],
            [0, 3, -3, 0, 0, 0],
            [1, 0, 0, 0, 2, -2],
            [0, 0, 0, 4, 0, 0],
            [0, -1, 1, 0, 0, 0],
            [0, 0, 0, 0, -3, 3],
            [5, 0, 0, -5, 0, 0],
        ]
    )
    return matrix.to_sparse()


def build_checkerboard_sparse(
    rows: int,
    cols: int,
    start_row: int,
    start_col: int,
    height: int,
    width: int,
    modulus: int,
    row_weight: int,
    col_weight: int,
    offset: int = 0,
) -> SparseMatrix:
    entries: list[SparseEntry] = []
    value_index = 0
    for dr in range(height):
        row = start_row + dr
        for dc in range(width):
            col = start_col + dc
            if (row_weight * dr + col_weight * dc) % modulus == 0:
                value = VALUE_CYCLE[(value_index + offset) % len(VALUE_CYCLE)]
                entries.append(SparseEntry(row, col, value))
                value_index += 1
    if not entries:
        raise ValueError("棋盘块至少需要一个元素")
    return SparseMatrix(rows, cols, entries)


def build_sparse_data5b() -> SparseMatrix:
    rows = cols = 1_000_000
    return build_checkerboard_sparse(
        rows=rows,
        cols=cols,
        start_row=200,
        start_col=400,
        height=30,
        width=27,
        modulus=5,
        row_weight=1,
        col_weight=1,
        offset=3,
    )


def build_sparse_data5c() -> SparseMatrix:
    rows = cols = 1_000_000
    start_row = 5_000
    row_count = 120
    start_col = 2_000
    entries: list[SparseEntry] = []
    value_index = 0
    for r_offset in range(row_count):
        row = start_row + r_offset
        for extra in (0, 1):
            col = start_col + r_offset * 3 + extra * 400
            value = VALUE_CYCLE[(value_index + extra) % len(VALUE_CYCLE)]
            if (r_offset + extra) % 2 == 1:
                value = -value
            entries.append(SparseEntry(row, col, value))
        value_index += 2
    return SparseMatrix(rows, cols, entries)


def build_sequences() -> dict[str, list[int]]:
    sequences: dict[str, list[int]] = {}

    small_dense = build_small_dense_matrix()
    medium_dense = build_medium_dense_matrix()
    small_sparse = small_dense.to_sparse()
    medium_sparse = medium_dense.to_sparse()

    sequences["data1a.txt"] = small_dense.to_format1()
    sequences["data1b.txt"] = medium_dense.to_format1()

    sequences["data2a.txt"] = small_sparse.to_format2()
    sequences["data2b.txt"] = medium_sparse.to_format2()
    sequences["data2c.txt"] = build_sparse_data2c().to_format2()

    sequences["data3a.txt"] = build_sparse_data3a().to_format3()
    sequences["data3b.txt"] = medium_sparse.to_format3()
    sequences["data3c.txt"] = build_sparse_data3c().to_format3()

    sequences["data4a.txt"] = build_sparse_data4a().to_format3()
    sequences["data4b.txt"] = build_sparse_data4b().to_format3()
    sequences["data4c.txt"] = build_sparse_data4c().to_format3()
    sequences["data4d.txt"] = build_sparse_data4d().to_format3()
    sequences["data4e.txt"] = build_sparse_data4e().to_format3()
    sequences["data4f.txt"] = build_sparse_data4f().to_format3()

    sequences["data5a.txt"] = build_sparse_data5a().to_format3()
    sequences["data5b.txt"] = build_sparse_data5b().to_format3()
    sequences["data5c.txt"] = build_sparse_data5c().to_format3()

    return sequences


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="为 reiwa7-natsu 题目生成测试数据")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="数据文件输出目录（默认为脚本所在目录）",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir: Path = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    sequences = build_sequences()
    for filename, sequence in sorted(sequences.items()):
        path = output_dir / filename
        write_sequence(path, sequence)
        print(f"{filename}: 写入 {len(sequence)} 个整数")


if __name__ == "__main__":
    main()
