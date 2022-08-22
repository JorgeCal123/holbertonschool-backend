#!/usr/bin/env python3
"""Simple Helper Function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    function named index_range that takes two
    integer arguments page and page_size
    """
    size_index = page * page_size
    index = size_index - page_size
    return (index, size_index)
