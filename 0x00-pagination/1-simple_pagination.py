import csv
import math
from typing import List, Tuple



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
        return  data[start: end]

def index_range(page: int, page_size: int) -> Tuple:
    """
    function named index_range that takes two 
    integer arguments page and page_size
    """
    size_index = page * page_size
    index = size_index - page_size
    return (index, size_index)
