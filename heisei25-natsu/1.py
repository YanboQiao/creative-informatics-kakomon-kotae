from pathlib import Path

import utils

def main():
    base_dir = Path(__file__).resolve().parent
    commands = utils.read_from_file(str(base_dir/'data'/'prog1.txt'))
    for command in commands:
        print(command[1])

if __name__ == "__main__":
    main()