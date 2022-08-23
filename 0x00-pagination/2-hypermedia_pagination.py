#!/usr/bin/env python3
"""class Server"""
import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get the list og page"""
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        assert page != 0
        assert page_size != 0
        [start, end] = index_range(page, page_size)
        data = self.dataset()
        return data[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """method that return a dict"""
        dict = {}
        dict['page_size'] = page_size
        dict['page'] = page
        dict['data'] = self.get_page(page, page_size)
        total_page = math.ceil(len(self.dataset()) / page_size)
        if (page < total_page):
            dict['next_page'] = page + 1
        else:
            dict['next_page'] = None
        if (page == 1 ):
            dict['prev_page'] = None
        else:
            dict['prev_page'] = page - 1
        dict['total_pages'] = total_page

        return dict

def index_range(page: int, page_size: int) -> Tuple:
    """
    function named index_range that takes two
    integer arguments page and page_size
    """
    size_index = page * page_size
    index = size_index - page_size
    return (index, size_index)
