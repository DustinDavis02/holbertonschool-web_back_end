#!/usr/bin/env python3
""" LIFOCache module """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class
    Inherits from BaseCaching and is a caching system implementing LIFO algorithm """
    
    def __init__(self):
        """ Initialize """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item value for the key key """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)

        if len(self.keys) > BaseCaching.MAX_ITEMS:
            discarded_key = self.keys.pop(-2)
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        return self.cache_data.get(key, None)
