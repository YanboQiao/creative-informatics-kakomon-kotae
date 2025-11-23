def area(hen: float) -> float:
    return hen * hen * (3 ** 0.5) / 4

def main():
    hen_length = 10.0
    hen_num = 3

    area_1 = area(hen_length)
    area_2 = area_1
    area_2 += 3 * area(hen_length / 3)
    print(area_1)
    print(area_2)

if __name__ == "__main__":
    main()