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

def get_max2(x: int, i: int, batt: list[Tuple[int,int]]) -> list[Tuple[int,int]]:
    for idx, (j, y) in enumerate(batt[:]):
        if x > y:
            batt[idx] = i, x
            return batt
        if i < j:
            return batt
    return batt

def process_input2(puzzle_input: str) -> int:
    total = 0
    for s in puzzle_input.splitlines():
        row = list(map(int,s))
        length = len(row)
        batt = [(idx, row[idx]) for idx in range(length-12,length)]
        for row_idx, x in enumerate(row):
            cap = length - row_idx
            if cap > 12:
                cap = 0
            else:
                cap = 12 - cap
            for batt_idx, (j, y) in enumerate(batt[cap:]):
                if x >= y:
                    if x == y and j < row_idx:
                        continue
                    batt[batt_idx + cap] = row_idx, x
                    break
                if row_idx < j:
                    break
        n = 0
        for i in range(12):
            n += batt[i][1] * (10 ** (11-i))
        total += n
    return total



                
                
    return total


def star1(puzzle_input: str) -> int:
    return process_input(puzzle_input)


def star2(puzzle_input: str) -> int:
    return process_input2(puzzle_input)


def run():
    print(star2(example_input))
    with open("input/day3.txt") as fp:
        pz_in = fp.read()        
        print(star1(pz_in))
        print(star2(pz_in))

        # 170870315881122 too high