#!/usr/bin/env python3
"""class FIFOCache"""
from base_caching import BaseCaching
import operator


class LFUCache(BaseCaching):
    """classFifoCache"""
    age_data = {}

    age = 0

    def __init__(self):
        """method constructor"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.age_data[key] = self.age
        self.age += 1
        sort_age = sorted(self.age_data.items(),
                          key=operator.itemgetter(1))

        if len(self.cache_data) > self.MAX_ITEMS:
            print("DISCARD: {}".format(next(iter(dict(sort_age)))))
            del self.cache_data[next(iter(dict(sort_age)))]
            del self.age_data[next(iter(dict(sort_age)))]

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.age_data[key] = self.age
        self.age += 1
        return self.cache_data[key]

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {} {}".format(key, self.cache_data.get(key), self.age_data[key]))

