#!/usr/bin/env python3
"""class FIFOCache"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """classFifoCache"""
    last_key = ""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        
        if len(self.cache_data) > self.MAX_ITEMS:
            print("DISCARD: {}".format(self.last_key))
            del self.cache_data[self.last_key]
        self.last_key = key

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
