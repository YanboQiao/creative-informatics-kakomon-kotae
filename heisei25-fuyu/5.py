import sympy as sym
import utils

sym.init_printing()


def main() -> None:
    formula = input().strip()

    # 调用工具函数求所有解
    DNF = utils.get_DNF(formula)

    if not DNF:
        print("none")
    else:
        print(DNF)


if __name__ == "__main__":
    main()
# (b&a+b&c+a)&b&c