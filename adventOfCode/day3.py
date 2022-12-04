from typing import Iterable
from adventOfCode.utils import open_puzzle_input
import pytest


def get_weird_ord(ch: str):
    if ord(ch) >= ord("a"):
        return ord(ch) - ord("a") + 1
    else:
        return ord(ch) - ord("A") + 1 + 26

def test_get_weird_ord():
    assert get_weird_ord("a") == 1
    assert get_weird_ord("z") == 26
    assert get_weird_ord("A") == 27
    assert get_weird_ord("B") == 28
    assert get_weird_ord("Z") == 52


def ex1(fp: Iterable[str]):
    sum_pr = 0
    for racksack in fp:
        if racksack.endswith("\n"):
            racksack = racksack[:-1]
        # import pdb; pdb.set_trace()
        assert len(racksack) % 2 == 0
        half_idx = len(racksack) // 2
        left, right = racksack[0:half_idx], racksack[half_idx:]
        left_set, right_set = set(left), set(right)
        shared_item = list(left_set.intersection(right_set))[0]
        sum_pr += get_weird_ord(shared_item)
    return sum_pr

def test_ex1():
    assert ex1([
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]) == 157


def ex2(fp: Iterable[str]):
    sum_pr = 0
    for idx, racksack in enumerate(fp):
        if racksack.endswith("\n"):
            racksack = racksack[:-1]
        if idx % 3 == 0:
            shared_set = set(racksack)
        else:
            shared_set = shared_set.intersection(set(racksack))
        if idx % 3 == 2:
            shared_item = list(shared_set)[0]
            sum_pr += get_weird_ord(shared_item)
    return sum_pr


def test_ex2():
    assert ex2([
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]) == 70




if __name__ == "__main__":
    with open_puzzle_input(day=3, year=2022) as fp:
        # print(ex1(fp))
        print(ex2(fp))


