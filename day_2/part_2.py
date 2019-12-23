from pathlib import Path
from typing import List


def run_program(memory: List[int]) -> List[int]:
    instruction_pointer = 0
    while True:
        opcode = memory[instruction_pointer]
        if opcode == 99:
            break
        input_pos_1 = memory[instruction_pointer + 1]
        input_pos_2 = memory[instruction_pointer + 2]
        output_pos = memory[instruction_pointer + 3]
        #print(opcode, input_pos_1, input_pos_2, output_pos)
        if opcode == 1:
            memory[output_pos] = memory[input_pos_1] + memory[input_pos_2]
            instruction_pointer += 4
        elif opcode == 2:
            memory[output_pos] = memory[input_pos_1] * memory[input_pos_2]
            instruction_pointer += 4
        else:
            raise Exception(f'Invalid opcode {opcode}')
    return memory


def run_program_on_input(program: List[int], noun: int, verb: int) -> int:
    memory = program.copy()
    memory[1] = noun
    memory[2] = verb
    result = run_program(memory)
    return result[0]


def main():
    input_path = Path('input.txt')
    input_text = input_path.read_text()
    program = [int(value) for value in input_text.split(',')]
    for noun in range(100):
        for verb in range(100):
            result = run_program_on_input(program, noun, verb)
            if result == 19690720:
                print(f'noun={noun}, verb={verb}')
                print(f'result={100 * noun + verb}')
                return
    raise Exception('Failed to find answer')


if __name__ == '__main__':
    main()
