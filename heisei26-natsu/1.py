def Apoint_number_R0(d: float) -> int:
    length: int = int(10 / d) + 1
    return length * length

def main():
    d: float = 1.0
    kotae = Apoint_number_R0(d)
    print(kotae)

if __name__ == "__main__":
    main()