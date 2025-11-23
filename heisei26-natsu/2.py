def Apoint_number_R1(d: float) -> int:
    kotae: int = 0
    length: int = int(10 / d) + 1
    for i in range(length):
        for j in range(length):
            x = i * d
            y = j * d
            kyori: float = (x - 5) * (x - 5) + (y - 5) * (y - 5)
            if kyori <= 25.0:
                kotae += 1
    return kotae

def main():
    d: float = 1.0
    a0: int = int(10 / d) + 1
    a0 *= a0
    a1= Apoint_number_R1(d)
    print(a1 / a0 * 0.25)

if __name__ == "__main__":
    main()