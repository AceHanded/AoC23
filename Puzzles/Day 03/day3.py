"""
Advent of Code - Day 3 puzzles
"""


with open("day3_input.txt") as input_file:
    puzzle_input = input_file.read().splitlines()

GEARS = {}
ADJACENT_COORDS = [-1, 0, 1]


def silver(inp: list[str]):
    """The silver star solution"""
    total_sum = 0

    for i, line in enumerate(inp):
        part_number, coord_ok = "", False

        for j, char in enumerate(line):
            if char.isdigit():
                part_number += char

                for y in ADJACENT_COORDS:
                    for x in ADJACENT_COORDS:
                        if 0 <= i + y < len(inp) and 0 <= j + x < len(line):
                            if not (inp[i + y][j + x] == "." or inp[i + y][j + x].isdigit()):
                                coord_ok = True

            if not char.isdigit() or j == len(line) - 1:
                total_sum += int(part_number) if coord_ok else 0
                part_number, coord_ok = "", False

    return total_sum


def gold(inp: list[str]):
    """The gold star solution"""
    total_sum = 0

    for i, line in enumerate(inp):
        part_number, coord_ok, gear = "", False, None

        for j, char in enumerate(line):
            if char.isdigit():
                part_number += char

                for y in ADJACENT_COORDS:
                    for x in ADJACENT_COORDS:
                        if 0 <= i + y < len(inp) and 0 <= j + x < len(line):
                            if inp[i + y][j + x] == "*":
                                gear = f"({i + y},{j + x})"

            if not char.isdigit() or j == len(line) - 1:
                if gear and gear not in GEARS:
                    GEARS[gear] = []
                if gear and gear in GEARS:
                    GEARS[gear].append(part_number)
                    total_sum += int(GEARS[gear][0]) * int(GEARS[gear][1]) if len(GEARS[gear]) == 2 else 0

                part_number, coord_ok, gear = "", False, None

    return total_sum


print(silver(puzzle_input))
print(gold(puzzle_input))
