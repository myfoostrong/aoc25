import sys
from typing import Tuple

from lib.num import is_odd

example_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

test_input = ""


def get_range(x: str, y: str) -> Tuple[str,str]:
    if is_odd(len(x)):
        if is_odd(len(y)):
            return "", ""
        else:
            new_x = str(10 ** (len(y)-1))
            return new_x, y
    if not is_odd(len(y)):
        return x, y
    new_y = str(10 ** (len(x)) - 1)
    return x, new_y


def process_input(puzzle_input: str) -> int:
    total = 0
    tracker = {}
    for s in puzzle_input.split(","):
        ids = s.split("-")
        x, y = get_range(ids[0],ids[1])
        if x == "":
            continue
        if len(y) - len(x) == 0 and is_odd(len(x)):
            continue
        half = len(x)//2
        x1 = x[:half]
        x2 = x[half:]
        y1 = y[:half]
        y2 = y[half:]
        x1i = int(x1)
        x2i = int(x2)
        y1i = int(y1)
        y2i = int(y2)
        # diff = y1i - x1i
        for a in range(x1i,y1i+1):
            if a == x1i:
                if x1i < x2i:
                    continue
            if a == y1i:
                if y1i > y2i:
                    continue
            z = a + a * (10 ** half)
            # if tracker.get(z) is None:
            #     tracker[z] = True
            total += z

        

    return total


def star1(puzzle_input: str) -> int:
    return process_input(puzzle_input)


def star2(puzzle_input: str) -> int:
    return process_input(puzzle_input)


def run():
    with open("input/day2.txt") as fp:
        pz_in = fp.read()
        print(star1(pz_in))

    # print(star1("11-22,95-115"))
    # print(star1(example_input))
    # 441089492933698 too high
    # 441068252721298 too high