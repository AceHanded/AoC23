"""
Advent of Code - Day 4 puzzles
"""


with open("day4_input.txt") as input_file:
    puzzle_input = input_file.read().splitlines()

WINNING_NUMBERS = set()
OWNED_NUMBERS = set()


def silver(inp: list[str]):
    """The silver star solution"""
    total_sum = 0

    for line in inp:
        WINNING_NUMBERS.clear(), OWNED_NUMBERS.clear()

        WINNING_NUMBERS.update(line.split("|")[0].split(":")[1].split())
        OWNED_NUMBERS.update(line.split("|")[1].split())

        winning_count = len(OWNED_NUMBERS.intersection(WINNING_NUMBERS)) - 1

        if winning_count >= 0:
            total_sum += 2 ** winning_count

    return total_sum


def gold(inp: list[str]):
    """The gold star solution"""
    total_sum = 0
    cards = {}

    for i, line in enumerate(inp):
        WINNING_NUMBERS.clear(), OWNED_NUMBERS.clear()

        cards[i] = cards.get(i, 0) + 1

        WINNING_NUMBERS.update(line.split("|")[0].split(":")[1].split())
        OWNED_NUMBERS.update(line.split("|")[1].split())

        winning_count = len(OWNED_NUMBERS.intersection(WINNING_NUMBERS))

        for j in range(winning_count):
            cards[i + j + 1] = cards.get(i + j + 1, 0) + cards[i]

    total_sum += sum(cards.values())

    return total_sum


print(silver(puzzle_input))
print(gold(puzzle_input))
