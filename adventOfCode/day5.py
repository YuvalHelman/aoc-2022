from typing import Callable, Iterable, Optional, Tuple, List
from adventOfCode.utils import open_puzzle_input
import pytest
import re

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def move_crates(crates_stacks: List[List[str]], quantity: int, from_line: int, to_line: int):
    try:
        for _ in range(quantity):
            crates_stacks[to_line - 1].append(crates_stacks[from_line - 1].pop())
    except Exception:
        print(f"failed moving crates with items: {quantity}, {from_line}, {to_line}")

def test_move_crates():
    crates = [
                [ "A", "B", "C" ],
                [ "D", "E", "F" ],
                [ "G", "H", "I" ],
            ]
    move_crates(crates, 2, 2, 1)
    assert crates[0] == ["A", "B", "C" , "F", "E"]
    assert crates[1] == ["D"]


def the_crate_machinary_script(fp: Iterable[str], move_crates_func: Callable):
    crates_stacks: Optional[List[List[str]]] = None
    is_crates_input = True
    for line in fp:
        if line == "\n":
            is_crates_input = False
        elif line.startswith(" 1"):
            pass
        elif is_crates_input:
            if crates_stacks is None:
                crates_stacks = [list() for _ in range(len(line) // 4)]
            for idx, group in enumerate(chunker(line, 4)):
                if group[1] != " ":
                    crates_stacks[idx].insert(0, group[1])
        else:  # rest of the input
            # import pdb; pdb.set_trace()
            quant, from_line, to_line = re.findall(r'[0-9]+', line)
            move_crates_func(crates_stacks, int(quant), int(from_line), int(to_line))
    # output:
    res = ""
    for crate in crates_stacks:
        if crate:
            res += crate[-1]
    return res


def ex1(fp: Iterable[str]):
    return the_crate_machinary_script(fp, move_crates)


def move_crates_9001(crates_stacks: List[List[str]], quantity: int, from_line: int, to_line: int):
    try:
        helper_stack = []
        for _ in range(quantity):
            helper_stack.append(crates_stacks[from_line - 1].pop())
        for _ in range(quantity):
            crates_stacks[to_line - 1].append(helper_stack.pop())
    except Exception:
        print(f"failed moving crates with items: {quantity}, {from_line}, {to_line}")


def ex2(fp: Iterable[str]):
    return the_crate_machinary_script(fp, move_crates_9001)


if __name__ == "__main__":
    with open_puzzle_input(day=5, year=2022) as fp:
        # print(ex1(fp))
        print(ex2(fp))




