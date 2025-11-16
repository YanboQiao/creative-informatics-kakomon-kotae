import sympy as sym
import utils

sym.init_printing()


def main() -> None:
    # 读取一行布尔公式，例如：b&a+b&c+a&b&c
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