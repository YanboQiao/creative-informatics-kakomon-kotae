from pathlib import Path

import utils
from LMachine_SMP import LMachine


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    program_path = base_dir / "data" / "prog4.txt"
    commands = utils.read_from_file(str(program_path))
    machine = LMachine(commands)
    machine.run()


if __name__ == "__main__":
    main()