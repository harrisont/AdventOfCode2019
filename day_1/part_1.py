from pathlib import Path


def calculate_module_fuel(mass: int) -> int:
    return mass // 3 - 2


def main():
    data_path = Path('data.txt')
    with data_path.open() as data_file:
        data_lines = data_file.readlines()

    masses = [int(line) for line in data_lines]
    fuels = [calculate_module_fuel(mass) for mass in masses]
    total_fuel = sum(fuels)
    print(total_fuel)


if __name__ == '__main__':
    main()
