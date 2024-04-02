#!/usr/bin/python3
"""
    a module that implements the solution for task 1
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
        This class inherits from a base class (BaseCaching)
    """
    def __init__(self):
        """
            Initialize
        """
        super().__init__()

    def put(self, key, item):
        """
            assign to the dictionary self.cache_data the item value
            for the key key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
            a method that gets an item from the dictionary
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
