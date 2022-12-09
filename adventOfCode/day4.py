from typing import Callable, Iterable, Tuple, List
from adventOfCode.utils import open_puzzle_input
import pytest
import re

def does_overlap_exactly(first: Tuple[int, int], second: Tuple[int, int]) -> bool:
    """
        first[0]                        first[1]
                 second[0]   second[1]
                         or
        second[0]                       second[1]
                first[0]    first[1]
    """
    return (first[0] <= second[0] and first[1] >= second[1]) or \
        (second[0] <= first[0] and second[1] >= first[1])

def find_overlaps(fp: Iterable[str], overlap_func: Callable):
    count = 0
    for line in fp:
        first_pair, second_pair = line.split(',')
        first_nums = re.findall(r'[0-9]+', first_pair)
        second_nums = re.findall(r'[0-9]+', second_pair)
        first_tuple = (first_nums[0], first_nums[1]) if len(first_nums) > 1 else (first_nums[0], first_nums[0])
        second_tuple = (second_nums[0], second_nums[1]) if len(second_nums) > 1 else (second_nums[0], second_nums[0])
        first_tuple = (int(first_tuple[0]), int(first_tuple[1]))
        second_tuple = (int(second_tuple[0]), int(second_tuple[1]))
        if overlap_func(first_tuple, second_tuple):
            count += 1
    return count


def ex1(fp: Iterable[str]):
    return find_overlaps(fp, does_overlap_exactly)

def test_ex1():
    assert ex1([
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8",
    ]) == 2

def does_overlap_atall(first: Tuple[int, int], second: Tuple[int, int]) -> bool:
    """
        first[0]                        first[1]
                 second[0]   second[1]
                         or
        second[0]                       second[1]
                first[0]    first[1]
    """
    return (second[0] <= first[0] <= second[1]) or \
            (first[0] <= second[0] <= first[1])


def ex2(fp: Iterable[str]):
    return find_overlaps(fp, does_overlap_atall)

def test_ex2():
    assert ex2([
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8",
    ]) == 4




if __name__ == "__main__":
    with open_puzzle_input(day=4, year=2022) as fp:
        # print(ex1(fp))
        print(ex2(fp))



