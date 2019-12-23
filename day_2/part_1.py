from pathlib import Path
from typing import List


def run_program(program: List[int]) -> List[int]:
    for i in range(0, len(program), 4):
        opcode = program[i]
        if opcode == 99:
            break
        input_pos_1 = program[i + 1]
        input_pos_2 = program[i + 2]
        output_pos = program[i + 3]
        #print(opcode, input_pos_1, input_pos_2, output_pos)
        if opcode == 1:
            program[output_pos] = program[input_pos_1] + program[input_pos_2]
        elif opcode == 2:
            program[output_pos] = program[input_pos_1] * program[input_pos_2]
        else:
            raise Exception(f'Invalid opcode {opcode}')
    return program


def main():
    input_path = Path('input.txt')
    input_text = input_path.read_text()
    program = [int(value) for value in input_text.split(',')]
    program[1] = 12
    program[2] = 2
    result = run_program(program)
    #print(result)
    print(result[0])


if __name__ == '__main__':
    main()
