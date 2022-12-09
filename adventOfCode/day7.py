from io import TextIOWrapper
from typing import List, Optional, Tuple, Iterable
from adventOfCode.utils import open_puzzle_input
import pytest
import re
from adventOfCode.log_util import aoc_parent_logger

import pdb

logger = aoc_parent_logger.getChild("day7")

class Node:
    def __init__(self, name: str, is_dir: bool = False, parent = None, size: int = 0) -> None:
        self.name = name
        self.size = size
        self.parent : Optional[Node] = parent
        self.children = list()
        self.is_dir = is_dir

class FsTree:
    def __init__(self, fp: TextIOWrapper) -> None:
        self.root: Node = Node("/", is_dir = True)
        self.fp = fp
        self.curr_node : Node = self.root
        self.command : List[str] = list()
        self.line = None

    def read_next_line_command(self) -> str:
        line = self.fp.readline()[:-1]
        if line:
            if line.startswith(r"$"):
                self.command = line.split(" ")[1:]
        self.line = line
        return self.line

    def build_fs_tree(self) -> None:
        self.read_next_line_command()
        while self.line:
            self.op_command()

    def op_command(self,):
        if self.command[0] == "cd":
            self.op_cd()
            self.read_next_line_command()
        if self.command[0] == "ls":
            self.op_ls()

    def op_cd(self,):
        if self.command[1] == "..":
            if self.curr_node == self.root:
                raise AssertionError(f"cd .. on root.. error: {self.command}")
            self.curr_node = self.curr_node.parent
        elif self.command[1] == r"/":
            self.curr_node = self.root
        else:
            if not self.curr_node.children:
                raise AssertionError(f"{self.command} where no children")
            for child_node in self.curr_node.children:
                if child_node.name == self.command[1]:
                    self.curr_node = child_node

    def op_ls(self,):
        self.read_next_line_command()
        while self.line and not self.line.startswith(r"$"):
            line = self.line.split(" ")
            size_or_dir, node_name = line[0], line[1]
            is_dir = size_or_dir == "dir"
            self.curr_node.children.append(Node(node_name, is_dir, self.curr_node, 0 if is_dir else int(size_or_dir)))
            self.read_next_line_command()

    def dfs_set_weights(self):
        stack = [self.root]
        visited = set()
        while stack:
            node = stack[-1]
            if node.is_dir:
                all_children_done = all([child in visited for child in node.children])
                if all_children_done:
                    node.size = sum([child.size for child in node.children])
                    visited.add(node)
                    stack.pop()
                else:
                    for child in node.children:
                        if child not in visited:
                            stack.append(child)
                            break
            else:
                visited.add(node)
                stack.pop()


    def get_sizes_sum_ofdirs_size_at_most(self, at_most_size: int):
        size_sum = 0
        stack = [self.root]
        visited = set()
        while stack:
            node = stack[-1]
            if node.is_dir:
                all_children_done = all([child in visited for child in node.children])
                if all_children_done:
                    if node.size <= at_most_size:
                        size_sum += node.size
                    visited.add(node)
                    stack.pop()
                else:
                    for child in node.children:
                        if child not in visited:
                            stack.append(child)
                            break
            else:
                visited.add(node)
                stack.pop()
        return size_sum

    def get_sizes_of_all_dirs(self) -> List[Tuple[str, int]]:
        size_per_dir = []
        stack = [self.root]
        visited = set()
        while stack:
            node = stack[-1]
            if node.is_dir:
                all_children_done = all([child in visited for child in node.children])
                if all_children_done:
                    size_per_dir.append((node.name, node.size))
                    visited.add(node)
                    stack.pop()
                else:
                    for child in node.children:
                        if child not in visited:
                            stack.append(child)
                            break
            else:
                visited.add(node)
                stack.pop()
        return size_per_dir


    def choose_dir_to_delete(self):
        size_per_dir = self.get_sizes_of_all_dirs()

        currently_unused_space: int = 70_000_000 - self.root.size
        needed_space = 30_000_000 - currently_unused_space
        size_per_dir = [item for item in size_per_dir if item[1] > needed_space]
        size_per_dir = sorted(size_per_dir, key=lambda x: x[1])
        return size_per_dir[0]



def main_logic(fp):
    fs = FsTree(fp)
    fs.build_fs_tree()
    logger.info("build fs tree done")
    fs.dfs_set_weights()
    logger.info("dfs set weights done")
    return fs


def ex1(fp):
    fs = main_logic(fp)
    res = fs.get_sizes_sum_ofdirs_size_at_most(100_000)
    logger.info("get sizes of size at most - done")
    return res


def ex2(fp: Iterable[str]):
    fs = main_logic(fp)
    return fs.choose_dir_to_delete()


if __name__ == "__main__":
    fetch_day_from_file_name = re.findall(r"\d+", str(__file__).split(r'/')[-1])[0]
    with open_puzzle_input(day=fetch_day_from_file_name, year=2022) as fp:
        # print(ex1(fp))
        print(ex2(fp))

