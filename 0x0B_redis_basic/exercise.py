#!/usr/bin/env python3
"""This module contains the Cache class for storing data."""

import redis
import uuid
from typing import Union

class Cache:
    """Cache class for storing data in database."""
    def __init__(self):
        """Initialize a Cache instance with a Redis client and flush the Redis instance."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the input data in Redis using a random key and return the key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

if __name__ == "__main__":
    # For initial testing purposes
    cache = Cache()
    data = b"hello"
    key = cache.store(data)
    print(key)
    local_redis = redis.Redis()
    print(local_redis.get(key))
