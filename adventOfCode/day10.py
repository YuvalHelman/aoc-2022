from io import TextIOWrapper
from pathlib import Path
from typing import Iterable
from adventOfCode.utils import open_puzzle_input
from adventOfCode.file_utils import fp_read_one_char_at_atime
import pytest
import re


def main_logic(fp: Iterable[str]):
    cycle_num = 0
    x = 1
    sum_strength = 0
    cycles = [20, 60, 100, 140, 180, 220]
    for line in fp:
        if line.startswith("noop"):
            cycle_num += 1
            if cycle_num in cycles:
                print(f"cycle_num {cycle_num}")
                print(f"x = {x}")
                print(f"signal strength: {cycle_num*x}")
                sum_strength += cycle_num * x
        elif line.startswith("addx"):
            op = re.findall(r'[-]?[0-9]+', line)[0]
            # import pdb; pdb.set_trace()
            cycle_num += 1
            if cycle_num in cycles:
                print(f"cycle_num {cycle_num}")
                print(f"x = {x}")
                print(f"signal strength: {cycle_num*x}")
                sum_strength += cycle_num * x
            cycle_num += 1
            x += int(op)
            if cycle_num in cycles:
                print(f"cycle_num {cycle_num}")
                print(f"x = {x}")
                print(f"signal strength: {cycle_num*x}")
                sum_strength += cycle_num * x
    return sum_strength


def ex1(fp: TextIOWrapper):
    return main_logic(fp)

def test_ex1():
    lines = [
        "addx 15",
        "addx -11",
        "addx 6",
        "addx -3",
        "addx 5",
        "addx -1",
        "addx -8",
        "addx 13",
        "addx 4",
        "noop",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx -35",
        "addx 1",
        "addx 24",
        "addx -19",
        "addx 1",
        "addx 16",
        "addx -11",
        "noop",
        "noop",
        "addx 21",
        "addx -15",
        "noop",
        "noop",
        "addx -3",
        "addx 9",
        "addx 1",
        "addx -3",
        "addx 8",
        "addx 1",
        "addx 5",
        "noop",
        "noop",
        "noop",
        "noop",
        "noop",
        "addx -36",
        "noop",
        "addx 1",
        "addx 7",
        "noop",
        "noop",
        "noop",
        "addx 2",
        "addx 6",
        "noop",
        "noop",
        "noop",
        "noop",
        "noop",
        "addx 1",
        "noop",
        "noop",
        "addx 7",
        "addx 1",
        "noop",
        "addx -13",
        "addx 13",
        "addx 7",
        "noop",
        "addx 1",
        "addx -33",
        "noop",
        "noop",
        "noop",
        "addx 2",
        "noop",
        "noop",
        "noop",
        "addx 8",
        "noop",
        "addx -1",
        "addx 2",
        "addx 1",
        "noop",
        "addx 17",
        "addx -9",
        "addx 1",
        "addx 1",
        "addx -3",
        "addx 11",
        "noop",
        "noop",
        "addx 1",
        "noop",
        "addx 1",
        "noop",
        "noop",
        "addx -13",
        "addx -19",
        "addx 1",
        "addx 3",
        "addx 26",
        "addx -30",
        "addx 12",
        "addx -1",
        "addx 3",
        "addx 1",
        "noop",
        "noop",
        "noop",
        "addx -9",
        "addx 18",
        "addx 1",
        "addx 2",
        "noop",
        "noop",
        "addx 9",
        "noop",
        "noop",
        "noop",
        "addx -1",
        "addx 2",
        "addx -37",
        "addx 1",
        "addx 3",
        "noop",
        "addx 15",
        "addx -21",
        "addx 22",
        "addx -6",
        "addx 1",
        "noop",
        "addx 2",
        "addx 1",
        "noop",
        "addx -10",
        "noop",
        "noop",
        "addx 20",
        "addx 1",
        "addx 2",
        "addx 2",
        "addx -6",
        "addx -11",
        "noop",
        "noop",
        "noop",
    ]
    assert ex1(lines) == 13140


def ex2(fp: Iterable[str]):
    return main_logic(fp)


if __name__ == "__main__":
    fetch_day_from_file_name = re.findall(r"\d+", str(__file__).split(r'/')[-1])[0]
    with open_puzzle_input(day=fetch_day_from_file_name, year=2022) as fp:
        print(ex1(fp))
        # print(ex2(fp))


