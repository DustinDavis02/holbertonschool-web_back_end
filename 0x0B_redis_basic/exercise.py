#!/usr/bin/env python3
"""This module contains the Cache class for storing data in Redis."""

import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional


# Decorators
def count_calls(method: Callable) -> Callable:
    """Increment the count each time a method is called."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Store the history of inputs and outputs for a method."""
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)
        return output
    return wrapper


# Cache Class
class Cache:
    """Class for storing data in a Redis database."""

    def __init__(self):
        """Initialize a Cache instance with a Redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the data in Redis using a random key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Get data from Redis and optionally apply conversion function."""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Get the data from Redis and convert it to a string."""
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Get the data from Redis and convert it to an integer."""
        return self.get(key, int)


# Utilities
def replay(method: Callable):
    """Display the history of calls for a particular function."""
    method_name = method.__qualname__
    input_key = f"{method_name}:inputs"
    output_key = f"{method_name}:outputs"

    redis_instance = method.__self__._redis

    inputs = redis_instance.lrange(input_key, 0, -1)
    outputs = redis_instance.lrange(output_key, 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")
    for in_arg, out_res in zip(inputs, outputs):
        print(f"{method_name}(*{in_arg.decode('utf-8')}) -> {out_res.decode('utf-8')}")
