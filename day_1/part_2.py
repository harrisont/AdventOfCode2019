from pathlib import Path


def calculate_mass_fuel(mass: int) -> int:
    return max(mass // 3 - 2, 0)


def calculate_module_fuel(module_mass: int) -> int:
    total_mass = 0
    fuel_mass = module_mass
    while fuel_mass > 0:
        fuel_mass = calculate_mass_fuel(fuel_mass)
        total_mass += fuel_mass
    return total_mass


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
