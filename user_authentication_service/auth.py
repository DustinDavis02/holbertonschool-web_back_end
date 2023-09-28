#!/usr/bin/env python3
"""This module contains utility functions for authentication."""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes password string and returns salted hash bytes.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
