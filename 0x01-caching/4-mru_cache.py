#!/usr/bin/env python3
"""class FIFOCache"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """classFifoCache"""
    mru = ""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            print("DISCARD: {}".format(self.mru))
            del self.cache_data[self.mru]
        self.mru = key

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.mru = key

        return self.cache_data[key]
