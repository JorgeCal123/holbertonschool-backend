#!/usr/bin/python3
"""Class BasicCache"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):

    def __init__(self):
        """method constructor"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
