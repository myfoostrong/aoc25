import re
import sys
from typing import Tuple

from lib.num import is_odd

example_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

test_input = ""


def check_number(x: int) -> bool:
    a = str(x)
    half = len(a) // 2
    if len(a) is not 2*half:
        return False
    b = a[:half]
    c = a[half:]
    return b == c

def process_input(puzzle_input: str) -> int:
    total = 0
    for s in puzzle_input.split(","):
        ids = list(map(int, s.split("-")))
        for x in range(ids[0],ids[1]+1):
            if check_number(x):
                total += x
    return total


def check_number2(x: int) -> bool:
    number = str(x)
    half = len(number) // 2
    for a in range(half+1):
        s = number[:a]
        pattern = f'^({re.escape(s)}){{2,}}$'
        if re.match(pattern, number) is not None:
            return True
    return False


def process_input2(puzzle_input: str) -> int:
    total = 0
    for s in puzzle_input.split(","):
        ids = list(map(int, s.split("-")))
        for x in range(ids[0],ids[1]+1):
            if check_number2(x):
                total += x
    return total


def star1(puzzle_input: str) -> int:
    return process_input(puzzle_input)


def star2(puzzle_input: str) -> int:
    return process_input2(puzzle_input)


def run():
    with open("input/day2.txt") as fp:
        pz_in = fp.read()
        print(star1(pz_in))
        print(star2(pz_in))