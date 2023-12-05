"""
Advent of Code - Day 5 puzzles
"""
from functools import reduce


with open("day5_input.txt") as input_file:
    puzzle_input = input_file.read().splitlines()

SEEDS = set()
MAPS = []


def set_correspondences(number, map_):
    for range_values in map_.split('\n')[2:-1]:
        destination, source, range_ = map(int, range_values.split())

        if source <= number < source + range_:
            return number - source + destination

    return number


def silver(inp: list[str]):
    """The silver star solution"""
    SEEDS.update(map(int, inp[0].split()[1:]))
    MAPS.extend("\n".join([";" if line == "" else line for line in inp[1:]]).split(";"))

    return min(reduce(set_correspondences, MAPS, seed) for seed in SEEDS)


def gold(inp: list[str]):
    """The gold star solution"""
    ...


print(silver(puzzle_input))
print(gold(puzzle_input))
