#!/usr/bin/python3
"""
    a module that implements the solution for task 4
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
        This class inherits from a base class (BaseCaching)
    """
    def __init__(self):
        """
            Initialize
        """
        super().__init__()
        self.data_order = [key for key in self.cache_data.keys()]
        self.new_cache_by_lru = {}

    def put(self, key, item):
        """
            assign to the dictionary self.cache_data the item value
            for the key. deletes the least recently used item in the
            dictionary if it is greater than MAX_ITEMS.
        """
        if key is None or item is None:
            return
        for key in self.data_order:
            self.new_cache_by_lru[key] = self.cache_data[key]
        # make the new item the most recently used
        self.new_cache_by_lru[key] = item
        self.cache_data = self.new_cache_by_lru

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # remove the least recently used item from the cached data
            first_key = list(self.cache_data.keys())[0]
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """
            a method that gets an item from the dictionary
        """
        if key is None or key not in self.cache_data:
            return None
        self.data = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = self.data

        return self.data
