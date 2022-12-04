from io import TextIOWrapper
from typing import List
from adventOfCode.utils import open_puzzle_input
import re

# A: Rock , B: Paper, C: Scissors
# X         Y         Z

m = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

def calc_turn(opponent_turn: str, my_turn: str):
    score = 0
    score += m[my_turn]

    opp = m[opponent_turn] % 3
    my = m[my_turn] % 3
    if opp == my:
        score += 3
    elif (opp + 1) % 3 == my:
        score += 6
    return score


def ex1(fp: TextIOWrapper):
    total_score = 0
    for line in fp:
        line_nums: List = re.findall(r'[A-Z]', line)
        total_score += calc_turn(line_nums[0], line_nums[1])
    return total_score


result_arr = [1, 2, 3]
def choose_my_turn(opponent_turn: str, result: str):
    # A: Rock , B: Paper, C: Scissors
    # X = lose  Y = Draw  Z = Win
    opp_val = m[opponent_turn] - 1 # A, X -> 1, lose
    if result == "X":
        return ((opp_val - 1) % 3) + 1
    elif result == "Y":
        return 3 + (opp_val + 1)
    elif result == "Z":
        return 6 + (((opp_val + 1) % 3) + 1)
    raise Exception("bad input")


def ex2(fp: TextIOWrapper):
    total_score = 0
    for line in fp:
        line_nums: List = re.findall(r'[A-Z]', line)
        total_score += choose_my_turn(line_nums[0], line_nums[1])
    return total_score




if __name__ == "__main__":
    assert calc_turn('A', 'X') == 4
    assert calc_turn('A', 'Y') == 8
    assert calc_turn('A', 'Z') == 3
    assert calc_turn('B', 'X') == 1
    assert calc_turn('B', 'Y') == 5
    assert calc_turn('B', 'Z') == 9
    assert calc_turn('C', 'X') == 7
    assert calc_turn('C', 'Y') == 2
    assert calc_turn('C', 'Z') == 6

    assert choose_my_turn('A', 'X') == 3
    assert choose_my_turn('A', 'Y') == 4 # Done
    assert choose_my_turn('A', 'Z') == 6 + 2
    assert choose_my_turn('B', 'X') == 1
    assert choose_my_turn('B', 'Y') == 5
    assert choose_my_turn('B', 'Z') == 9
    assert choose_my_turn('C', 'X') == 2
    assert choose_my_turn('C', 'Z') == 6 + 1
    assert choose_my_turn('C', 'Y') == 6

    with open_puzzle_input(day=2, year=2022) as fp:
        # print(ex1(fp))
        print(ex2(fp))

