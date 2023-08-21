#!/usr/bin/env python3
"""A simple pagination helper function"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a two-dimensional tuple containing a start index and an end index"""

    return (page * page_size - page_size, page * page_size)
