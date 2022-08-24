#!/usr/bin/env python3
"""class FIFOCache"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """classFifoCache"""
    def __init__(self):
        super().__init__()
    
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            print("DISCARD: {}".format(next(iter(self.cache_data))))
            del self.cache_data[next(iter(self.cache_data))]

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
