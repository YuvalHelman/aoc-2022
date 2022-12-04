from typing import List
from adventOfCode.utils import open_puzzle_input


def day1_1(input_lines: List[str]):
    lines = input_lines
    dwarf_sum, dwarf_max_sum = 0, 0
    for i in range(len(lines)):
        if lines[i] != "\n":
            dwarf_sum += int(lines[i][:-1])
            dwarf_max_sum = max(dwarf_max_sum, dwarf_sum)
        else:
            dwarf_sum = 0
    return dwarf_max_sum

def day1_2(lines: List[str]):
    dwarf_sum = 0
    dwarf_max_sum_arr = [-1, -1, -1]
    for i in range(len(lines)):
        if lines[i] != "\n":
            dwarf_sum += int(lines[i][:-1])
        else:
            if dwarf_sum > dwarf_max_sum_arr[0]:
                dwarf_max_sum_arr.append(dwarf_sum)
                dwarf_max_sum_arr.sort()  # sort ascending order
                dwarf_max_sum_arr.pop(0)
            dwarf_sum = 0
    return sum(dwarf_max_sum_arr)


if __name__ == "__main__":
    with open_puzzle_input(day=1, year=2022) as fp:
        for i, line in enumerate(fp):
            print(line)
            break
        # lines = fp.readlines()
        # print(day1_1(lines))
        # print(day1_2(lines))
