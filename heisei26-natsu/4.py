def calculate(n: int):
    if n == 0:
        return 25 * (3 ** 0.5)
    if n > 0:
        return 25 * (3 ** 0.5) + 25 * (3 ** -0.5) * ((1 - (4 / 9) ** n) / (5 / 9))
    
def main():
    n = 1
    print(calculate(n))

if __name__ == "__main__":
    main()