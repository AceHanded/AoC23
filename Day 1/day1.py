"""
Advent of Code - Day 1 puzzles
"""


with open("day1_input.txt") as input_file:
    puzzle_input = input_file.read().splitlines()

spelt_digits = {"one": "1", "two": "2", "three": "3",
                "four": "4", "five": "5", "six": "6",
                "seven": "7", "eight": "8", "nine": "9"}


def silver(inp: list[str]):
    """The silver star solution"""
    total_sum = 0

    for line in inp:
        line_chars = []

        for i in range(len(line)):
            if line[i].isdigit():
                line_chars.append(line[i])

        total_sum += int(line_chars[0] + line_chars[-1])

    return total_sum


def gold(inp: list[str]):
    """The gold star solution"""
    total_sum = 0

    for line in inp:
        line_chars = []
        char_list = list(line)

        for i in range(len(line)):
            if line[i].isdigit():
                line_chars.append(line[i])
                continue

            for digit in spelt_digits:
                if list(digit) == char_list[i:i + len(digit)]:
                    line_chars.append(spelt_digits[digit])

        total_sum += int(line_chars[0] + line_chars[-1])

    return total_sum


print(silver(puzzle_input))
print(gold(puzzle_input))
