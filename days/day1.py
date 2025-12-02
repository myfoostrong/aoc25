import sys
from typing import Tuple

example_input = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

test_input = """
L48
L3
R2
L1
R2
L2
"""

def get_val(s: str) -> int:
    x = int(s[1:])
    if s[0] == "R":
        return x
    return -x


def get_pos(curr_pos: int, s: str) -> int:
    return (get_val(s) + curr_pos) % 100


def get_pos2(curr_pos: int, s: str) -> Tuple[int,int]:
    x = get_val(s)
    new_pos = curr_pos + x
    count = abs(new_pos // 100)
    if curr_pos == 0 and x < 0 and count > 0:
        count-=1
    adj_pos = new_pos % 100
    if adj_pos == 0 and new_pos < 100:
        count +=1
    return adj_pos, count


def parse_input(s: str) -> list[str]:
    return s.splitlines()


def process_input(input: list[str]) -> int:
    pos = 50
    count = 0
    for s in input:
        if s == "":
            continue
        pos = get_pos(pos, s)
        if pos == 0:
            count+=1
    return count


def process_input2(input: list[str]) -> int:
    pos = 50
    count = 0
    for s in input:
        if s == "":
            continue
        pos, ticks = get_pos2(pos, s)
        count += ticks
    return count

def star1(input: str) -> int:
    return process_input(parse_input(input))


def star2(input: str) -> int:
    return process_input2(parse_input(input))

if __name__ == "__main__":
    print(star1(example_input))
    print(star2(example_input))
    with open("input/day1.txt") as fp:
        input = fp.read()
        print(star1(input))
        print(star2(input))