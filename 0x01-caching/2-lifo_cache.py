#!/usr/bin/python3
"""
    a module that implements the solution for task 3
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
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
            for the key. deletes the last item in the dictionary if
            it is greater than MAX_ITEMS
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-2]
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

    def get(self, key):
        """
            a method that gets an item from the dictionary
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
