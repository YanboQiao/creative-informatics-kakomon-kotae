import sympy as sym
import utils

sym.init_printing()


def main() -> None:
    formula = input().strip()

    # 调用工具函数求所有解
    solutions = utils.get_kai(formula)

    if not solutions:
        print("none")
    else:
        for line in solutions:
            print(line)


if __name__ == "__main__":
    main()
# (b&a+b&c+a)&b&c