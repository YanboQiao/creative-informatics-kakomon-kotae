import sympy as sym
import utils

sym.init_printing()


def main() -> None:
    formula = input().strip()

    # 调用工具函数求所有解
    CNF = utils.get_CNF(formula)

    if not CNF:
        print("none")
    else:
        print(CNF)


if __name__ == "__main__":
    main()
# (b&a+b&c+a)&b&c