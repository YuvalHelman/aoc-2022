from typing import Iterable
from adventOfCode.utils import open_puzzle_input
from adventOfCode.file_utils import fp_read_one_char_at_atime
import pytest
import re

def message_finder(fp: Iterable[str], message_len: int):
    str_so_far = ""
    for idx, char in enumerate(fp):
        str_so_far += char
        if len(str_so_far) > message_len:
            str_so_far = str_so_far[1:]
        if len(str_so_far) == message_len and len(set(str_so_far)) == message_len:
            return idx + 1
    return -1


def ex1(fp: Iterable[str]):
    return message_finder(fp, 4)

def test_ex1():
    assert ex1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert ex1("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert ex1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert ex1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11




def ex2(fp: Iterable[str]):
    return message_finder(fp, 14)


def test_ex2():
    assert ex2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert ex2("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert ex2("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert ex2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert ex2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26


if __name__ == "__main__":
    with open_puzzle_input(day=6, year=2022) as fp:
        # print(ex1(fp_read_one_char_at_atime(fp)))
        print(ex2(fp_read_one_char_at_atime(fp)))





