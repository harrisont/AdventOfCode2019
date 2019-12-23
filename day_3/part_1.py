import enum
from pathlib import Path
from typing import List, Tuple


INTERSECTION_VALUE = 9


class Direction(enum.Enum):
    U = enum.auto()
    D = enum.auto()
    L = enum.auto()
    R = enum.auto()


class Instruction:
    def __init__(self, direction: Direction, num: int):
        self.direction = direction
        self.num = num

    def __repr__(self) -> str:
        return f'{self.direction.name}{self.num}'


def parse_instruction(instruction: str) -> Instruction:
    direction = Direction[instruction[0]]
    num = int(instruction[1:])
    return Instruction(direction, num)


def get_position_after_instruction(x: int,
                                   y: int,
                                   instruction: Instruction) -> (int, int):
    """
    :return: (x', y', direction_x, direction_y)
    """
    if instruction.direction == Direction.L:
        return x - instruction.num, y, -1, 0
    elif instruction.direction == Direction.R:
        return x + instruction.num, y, 1, 0
    elif instruction.direction == Direction.D:
        return x, y - instruction.num, 0, -1
    elif instruction.direction == Direction.U:
        return x, y + instruction.num, 0, 1


def calc_board_size(paths: List[List[Instruction]]) -> (int, int, int, int):
    """
    :return: (size_x, size_y, center_x, center_y)
    """
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    for path in paths:
        current_x = 0
        current_y = 0
        for instruction in path:
            current_x, current_y, _, _ = get_position_after_instruction(current_x, current_y, instruction)
            if current_x < min_x:
                min_x = current_x
            elif current_x > max_x:
                max_x = current_x
            if current_y < min_y:
                min_y = current_y
            elif current_y > max_y:
                max_y = current_y
    size_x = max_x - min_x + 1
    size_y = max_y - min_y + 1
    return size_x, size_y, -min_x, -min_y


def space_str(value: int) -> str:
    if value == 0:
        return ' '
    elif value == INTERSECTION_VALUE:
        return 'X'
    else:
        return str(value)


def print_board(board: List[List[int]]) -> None:
    for y in range(len(board) - 1, -1, -1):
        print(''.join((space_str(x) for x in board[y])))
    print()


def trace_paths(board: List[List[int]],
                center_x: int,
                center_y: int,
                paths: List[List[Instruction]]
                ) -> List[Tuple[int, int]]:
    """
    :return: List[(intersection_x, intersection_y)]
    """
    intersections: List[Tuple[int, int]] = []
    for path_index, path in enumerate(paths):
        path_id = path_index + 1
        current_x = center_x
        current_y = center_y
        for instruction in path:
            new_x, new_y, direction_x, direction_y = get_position_after_instruction(current_x, current_y, instruction)
            while current_x != new_x or current_y != new_y:
                current_x += direction_x
                current_y += direction_y
                current_value = board[current_y][current_x]
                if current_value > 0 and current_value != path_id:
                    board[current_y][current_x] = INTERSECTION_VALUE
                    intersections.append((current_x, current_y))
                else:
                    board[current_y][current_x] = path_id
        #print_board(board)
    return intersections


def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x2 - x1) + abs(y2 - y1)


def main():
    input_path = Path('input.txt')
    with input_path.open() as input_file:
        input_lines = input_file.readlines()

    #input_lines = [
        #'R8,U5,L5,D3',
        #'U7,R6,D4,L4',

        #'R75,D30,R83,U83,L12,D49,R71,U7,L72',
        #'U62,R66,U55,R34,D71,R55,D58,R83',

        #'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
        #'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7',
    #]

    paths: List[List[Instruction]] = []
    for input_line in input_lines:
        instruction_strs = input_line.split(',')
        path = [parse_instruction(instruction_str) for instruction_str in instruction_strs]
        paths.append(path)

    size_x, size_y, center_x, center_y = calc_board_size(paths)
    #print('size:', size_x, size_y)

    board = [[0 for x in range(size_x)] for y in range(size_y)]
    intersections = trace_paths(board, center_x, center_y, paths)
    #print_board(board)

    #for intersection_x, intersection_y in intersections:
    #    print(intersection_x, intersection_y)
    distances = [manhattan_distance(center_x, center_y, x, y) for x, y in intersections]
    #print(distances)
    min_distance = min(distances)
    print(min_distance)


if __name__ == '__main__':
    main()
