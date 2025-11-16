import utils

def main():
    formula = 'b&a+b&c+a&b&c'
    splited = utils.split_formula(formula)
    for seperated in splited:
        print(seperated)

if __name__ == "__main__":
    main()