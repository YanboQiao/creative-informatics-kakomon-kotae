# -*- coding: utf-8 -*-
"""
单断点分段线性回归（连续性约束，最小平方误差）+ 随机数据生成 + 可视化
"""

from __future__ import annotations
from typing import List, Tuple
import math
import random
import matplotlib.pyplot as plt


def generate_points(n: int = 30, seed: int = 42) -> List[Tuple[int, int]]:
    """
    随机生成 n 个数据点 (x, y)，0<=x<30, 0<=y<30。
    模拟两段线性关系并添加少量噪声。
    """
    random.seed(seed)
    pts: List[Tuple[int, int]] = []
    for i in range(n):
        x = i
        if x < n // 2:
            y = 0.8 * x + 5 + random.uniform(-2, 2)
        else:
            y = 0.8 * x + 15 + random.uniform(-2, 2)
        pts.append((x, y))
    return pts


def get_two_line(ten: List[Tuple[int, int]]) -> Tuple[float, float, float, float, float]:
    pts = sorted((float(x), float(y)) for x, y in ten)
    n = len(pts)
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]

    if n <= 1:
        return 0.0, 0.0, 0.0, 0.0, 0.0

    sx = [0.0] * n
    sy = [0.0] * n
    sx2 = [0.0] * n
    sxy = [0.0] * n
    sy2 = [0.0] * n
    s1 = s2 = s3 = s4 = s5 = 0.0
    for i, (x, y) in enumerate(zip(xs, ys)):
        s1 += x
        s2 += y
        s3 += x * x
        s4 += x * y
        s5 += y * y
        sx[i], sy[i], sx2[i], sxy[i], sy2[i] = s1, s2, s3, s4, s5
    total = dict(sx=sx[-1], sy=sy[-1], sx2=sx2[-1], sxy=sxy[-1], sy2=sy2[-1])
    cut_positions = [j for j in range(n - 1) if xs[j] < xs[j + 1]]
    if not cut_positions:
        y_mean = total["sy"] / n
        return 0.0, y_mean, 0.0, y_mean, xs[0]

    eps = 1e-9
    phi = (math.sqrt(5.0) - 1.0) / 2.0

    def sums_left(j: int):
        L = j + 1
        return L, sx[j], sy[j], sx2[j], sxy[j], sy2[j]

    def sums_right(j: int):
        R = n - (j + 1)
        return (
            R,
            total["sx"] - sx[j],
            total["sy"] - sy[j],
            total["sx2"] - sx2[j],
            total["sxy"] - sxy[j],
            total["sy2"] - sy2[j],
        )

    def coeffs(L, SxL, SyL, Sx2L, SxyL, Sy2L,
               R, SxR, SyR, Sx2R, SxyR, Sy2R, xm: float):
        SxxL = Sx2L - 2 * xm * SxL + L * xm * xm
        sum_uL = SxL - L * xm
        TxyL = SxyL - xm * SyL
        SxxR = Sx2R - 2 * xm * SxR + R * xm * xm
        sum_vR = SxR - R * xm
        TxyR = SxyR - xm * SyR
        if SxxL <= 1e-12 or SxxR <= 1e-12:
            return None
        A0L = Sy2L - (TxyL * TxyL) / SxxL
        A1L = -2 * SyL + 2 * (sum_uL * TxyL) / SxxL
        A2L = L - (sum_uL * sum_uL) / SxxL
        A0R = Sy2R - (TxyR * TxyR) / SxxR
        A1R = -2 * SyR + 2 * (sum_vR * TxyR) / SxxR
        A2R = R - (sum_vR * sum_vR) / SxxR
        c0 = A0L + A0R
        c1 = A1L + A1R
        c2 = A2L + A2R
        return c0, c1, c2, SxxL, sum_uL, TxyL, SxxR, sum_vR, TxyR

    best_SSE = float("inf")
    best_pack = None

    for j in cut_positions:
        L, SxL, SyL, Sx2L, SxyL, Sy2L = sums_left(j)
        R, SxR, SyR, Sx2R, SxyR, Sy2R = sums_right(j)
        lo, hi = xs[j] + eps, xs[j + 1] - eps
        if lo >= hi:
            continue

        def E_at(xm: float):
            res = coeffs(L, SxL, SyL, Sx2L, SxyL, Sy2L,
                         R, SxR, SyR, Sx2R, SxyR, Sy2R, xm)
            if res is None:
                return float("inf"), None, None
            c0, c1, c2, SxxL, sum_uL, TxyL, SxxR, sum_vR, TxyR = res
            if c2 <= 1e-15:
                ym = (SyL + SyR) / (L + R)
                SSE = c0
            else:
                ym = -c1 / (2 * c2)
                SSE = c0 - (c1 * c1) / (4 * c2)
            return SSE, ym, (SxxL, sum_uL, TxyL, SxxR, sum_vR, TxyR)

        x1, x2 = hi - phi * (hi - lo), lo + phi * (hi - lo)
        f1, y1, s1 = E_at(x1)
        f2, y2, s2 = E_at(x2)
        best_local = (f1, x1, y1, s1) if f1 < f2 else (f2, x2, y2, s2)
        for _ in range(60):
            if f1 > f2:
                lo, x1, f1, y1, s1 = x1, x2, f2, y2, s2
                x2 = lo + phi * (hi - lo)
                f2, y2, s2 = E_at(x2)
            else:
                hi, x2, f2, y2, s2 = x2, x1, f1, y1, s1
                x1 = hi - phi * (hi - lo)
                f1, y1, s1 = E_at(x1)
            if hi - lo < 1e-10:
                break
            if f1 < best_local[0]:
                best_local = (f1, x1, y1, s1)
            if f2 < best_local[0]:
                best_local = (f2, x2, y2, s2)
        SSE_best, xm_best, ym_best, stats_best = best_local
        if SSE_best < best_SSE:
            best_SSE = SSE_best
            best_pack = (xm_best, ym_best, stats_best,
                         (L, SxL, SyL, Sx2L, SxyL, Sy2L),
                         (R, SxR, SyR, Sx2R, SxyR, Sy2R))
    if best_pack is None:
        y_mean = sum(ys) / n
        return 0.0, y_mean, 0.0, y_mean, xs[n // 2]

    xm, ym, stats, Ls, Rs = best_pack
    L, SxL, SyL, Sx2L, SxyL, Sy2L = Ls
    R, SxR, SyR, Sx2R, SxyR, Sy2R = Rs
    SxxL, sum_uL, TxyL, SxxR, sum_vR, TxyR = stats
    a1 = (TxyL - ym * sum_uL) / SxxL
    a2 = (TxyR - ym * sum_vR) / SxxR
    b1 = ym - a1 * xm
    b2 = ym - a2 * xm
    return a1, b1, a2, b2, xm


def plot_piecewise(points: List[Tuple[int, int]],
                   a1: float, b1: float, a2: float, b2: float, xm: float) -> None:
    xs = [float(x) for x, _ in points]
    ys = [float(y) for _, y in points]
    plt.figure(figsize=(6, 6))
    plt.scatter(xs, ys, s=40, label="data")
    x_min, x_max = min(xs), max(xs)
    y_m = a1 * xm + b1
    xl = [x_min, xm]
    yl = [a1 * xl[0] + b1, a1 * xl[1] + b1]
    xr = [xm, x_max]
    yr = [a2 * xr[0] + b2, a2 * xr[1] + b2]
    plt.plot(xl, yl, label=f"left: y={a1:.2f}x+{b1:.2f}")
    plt.plot(xr, yr, label=f"right: y={a2:.2f}x+{b2:.2f}")
    plt.scatter([xm], [y_m], marker="x", s=100, linewidths=2, label=f"break xm={xm:.2f}")
    plt.xlim(0, 50)
    plt.ylim(0, 50)
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    pts = generate_points()
    a1, b1, a2, b2, xm = get_two_line(pts)
    print(f"a1={a1:.4f}, b1={b1:.4f}, a2={a2:.4f}, b2={b2:.4f}, xm={xm:.4f}")
    plot_piecewise(pts, a1, b1, a2, b2, xm)
