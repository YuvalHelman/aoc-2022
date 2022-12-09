from io import TextIOWrapper
from pathlib import Path
from typing import Iterable, List
from adventOfCode.utils import open_puzzle_input
import pytest
import re
import numpy as np


def main_logic(mat: List[List[int]]):
    n, m = len(mat), len(mat[0])
    res_mat = [[0 for _ in range(m)] for _ in range(n)]
    # left to right
    for i in range(n):
        max_so_far = -1
        for j in range(m):
            if mat[i][j] > max_so_far:
                max_so_far = mat[i][j]
                res_mat[i][j] = 1
    # right to left
    for i in range(n):
        max_so_far = -1
        for j in range(m-1, -1, -1):
            if mat[i][j] > max_so_far:
                max_so_far = mat[i][j]
                res_mat[i][j] = 1
    # top to bottom
    for j in range(m):
        max_so_far = -1
        for i in range(n):
            if mat[i][j] > max_so_far:
                max_so_far = mat[i][j]
                res_mat[i][j] = 1
    # bottom to top
    for j in range(m):
        max_so_far = -1
        for i in range(n-1, -1, -1):
            if mat[i][j] > max_so_far:
                max_so_far = mat[i][j]
                res_mat[i][j] = 1

    return np.sum(res_mat)


def ex1(fp: TextIOWrapper):
    mat = []
    for line in fp:
        line = line[:-1]  # ommit \n
        mat.append([int(num) for num in line])
    return main_logic(mat)

def test_ex1():
    mat= [
            [int(num) for num in list("30373")],
            [int(num) for num in list("25512")],
            [int(num) for num in list("65332")],
            [int(num) for num in list("33549")],
            [int(num) for num in list("35390")],
    ]
    assert main_logic(mat) == 21

def ex2(fp: Iterable[str]):
    return main_logic(fp)


if __name__ == "__main__":
    fetch_day_from_file_name = re.findall(r"\d+", str(__file__).split(r'/')[-1])[0]
    with open_puzzle_input(day=fetch_day_from_file_name, year=2022) as fp:
        print(ex1(fp))
        # print(ex2(fp))


