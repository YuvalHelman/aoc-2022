from io import TextIOWrapper
from pathlib import Path
from typing import Iterable
from adventOfCode.utils import open_puzzle_input
from adventOfCode.file_utils import fp_read_one_char_at_atime
import pytest
import re


def main_logic(fp: Iterable[str]):
    pass

def ex1(fp: TextIOWrapper):
    return main_logic(fp)


def ex2(fp: Iterable[str]):
    return main_logic(fp)


if __name__ == "__main__":
    fetch_day_from_file_name = re.findall(r"\d+", str(__file__).split(r'/')[-1])[0]
    with open_puzzle_input(day=fetch_day_from_file_name, year=2022) as fp:
        print(ex1(fp))
        # print(ex2(fp))


