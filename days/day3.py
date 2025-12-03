import re
import sys
from typing import Tuple

from lib.num import is_odd

example_input = """987654321111111
811111111111119
234234234234278
818181911112111"""

def process_input(puzzle_input: str) -> int:
    total = 0
    for s in puzzle_input.splitlines():
        a = s
    return total



def process_input2(puzzle_input: str) -> int:
    total = 0
    for s in puzzle_input.splitlines():
        a = s
    return total


def star1(puzzle_input: str) -> int:
    return process_input(puzzle_input)


def star2(puzzle_input: str) -> int:
    return process_input2(puzzle_input)


def run():
    with open("input/day3.txt") as fp:
        pz_in = fp.read()
        print(star1(pz_in))
        print(star2(pz_in))