import re
import sys
from typing import Tuple

from lib.num import is_odd

example_input = """987654321111111
811111111111119
234234234234278
818181911112111"""

def get_max(x: str, y: str, a: str) -> Tuple[str,str]:
    if a > x:
        return a, "0"
    if a > y:
        return x, a
    return x, y

def process_input(puzzle_input: str) -> int:
    total = 0
    for s in puzzle_input.splitlines():
        x, y = "0", "0"
        for i, a in enumerate(s):
            if i == len(s)-1:
                if a > y:
                    y = a
                break
            x, y = get_max(x,y,a)
        total += 10*int(x) + int(y)
    return total

def get_max2(x: str, y: str, a: str) -> Tuple[str,str]:
    if a > x:
        return a, 0
    if a > y:
        return x, a
    return x, y

def process_input2(puzzle_input: str) -> int:
    total = 0
    for s in puzzle_input.splitlines():
        
        for i, a in enumerate(list(map(int,s))):
            if i == len(s)-13:
                if a > y:
                    y = a
                break
            x, y = get_max2(x,y,a)
        total += 10*int(x) + int(y)
    return total


def star1(puzzle_input: str) -> int:
    return process_input(puzzle_input)


def star2(puzzle_input: str) -> int:
    return process_input2(puzzle_input)


def run():
    with open("input/day3.txt") as fp:
        pz_in = fp.read()
        
        print(star1(pz_in))
        # print(star2(pz_in))