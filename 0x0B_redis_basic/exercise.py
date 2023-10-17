#!/usr/bin/env python3
"""This module contains the Cache class for storing data."""

import redis
import uuid
from typing import Union, Callable, Optional

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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Get the data from Redis and apply a conversion function."""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Get the data from Redis and convert it to str."""
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Get the data from Redis and convert it to int."""
        return self.get(key, int)
