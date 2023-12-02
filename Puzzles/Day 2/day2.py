"""
Advent of Code - Day 2 puzzles
"""


with open("day2_input.txt") as input_file:
    puzzle_input = input_file.read().splitlines()

CUBES = {}


def silver(inp: list[str]):
    """The silver star solution"""
    total_sum = 0

    for line in inp:
        game_ok = True

        for subset in line.split(":")[1].split(";"):
            CUBES["red"], CUBES["green"], CUBES["blue"] = 0, 0, 0

            for cube in subset.split(","):
                CUBES[cube.split()[1].strip()] += int(cube.split()[0].strip())

            if not (CUBES["red"] > 12 or CUBES["green"] > 13 or CUBES["blue"] > 14):
                continue
            else:
                game_ok = False
                break

        if game_ok:
            total_sum += int(line.split()[1].strip()[:-1])

    return total_sum


def gold(inp: list[str]):
    """The gold star solution"""
    total_sum = 0

    for line in inp:
        max_red, max_green, max_blue = 0, 0, 0

        for subset in line.split(":")[1].split(";"):
            CUBES["red"], CUBES["green"], CUBES["blue"] = 0, 0, 0

            for cube in subset.split(","):
                CUBES[cube.split()[1].strip()] += int(cube.split()[0].strip())

            if CUBES["red"] > max_red:
                max_red = CUBES["red"]
            if CUBES["green"] > max_green:
                max_green = CUBES["green"]
            if CUBES["blue"] > max_blue:
                max_blue = CUBES["blue"]

        total_sum += max_red * max_green * max_blue

    return total_sum


print(silver(puzzle_input))
print(gold(puzzle_input))
