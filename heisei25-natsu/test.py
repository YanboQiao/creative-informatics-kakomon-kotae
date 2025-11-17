def mul_by_add(a: int, b: int) -> int:
    """
    使用重复加法实现乘法，对应 prog5.txt 中 SUB/BAK 那段循环的语义。
    逻辑等价于：acc = a * b
    """
    acc = 0
    while b != 0:
        acc += a
        b -= 1
    return acc


def fact_like_prog5(n: int) -> int:
    """
    阶乘函数，对应 prog5.txt 中以 in 为输入的 fact 子程序：
    if n == 0: return 1
    else: return n * fact(n - 1)
    其中乘法用 mul_by_add 模拟 SUB/BAK 的循环。
    """
    if n == 0:
        return 1
    # 对应 CAL -8 t 得到 fone = fact(n-1)
    fone = fact_like_prog5(n - 1)
    # 对应 a = n, b = fone，然后通过 SUB/BAK 循环做乘法
    return mul_by_add(n, fone)


def fib_like_prog5(n: int) -> int:
    """
    斐波那契函数，对应 prog5.txt 中的 fib 子程序：
    if n == 0: return 0
    if n == 1: return 1
    else: return fib(n-1) + fib(n-2)
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    f1 = fib_like_prog5(n - 1)
    f2 = fib_like_prog5(n - 2)
    return f1 + f2


def main() -> None:
    # 对应 prog5.txt 顶层：SET a 999, SET n 6, CAL fact, SET m 8, CAL fib, 然后 h = f + a, PRN h g
    a = 999
    n = 6
    f = fact_like_prog5(n)   # out of fact
    m = 8
    g = fib_like_prog5(m)    # out of fib
    h = f + a

    # 打印结果，与 LMachine 的 PRN h g 对应
    print(h, g)

    # 验证是否与预期一致
    assert h == 1719, f"h 应该是 1719, 实际为 {h}"
    assert g == 21, f"g 应该是 21, 实际为 {g}"


if __name__ == "__main__":
    main()
