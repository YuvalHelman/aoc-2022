from io import TextIOWrapper
from typing import Generator


def fp_read_one_char_at_atime(fp: TextIOWrapper) -> Generator[str, None, None]:
    while True:
        # read next character
        char = fp.read(1)
        # if not EOF, then at least 1 character was read, and 
        # this is not empty
        if char:
            yield char
        else:
            return
