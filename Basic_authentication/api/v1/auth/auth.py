#!/usr/bin/env python3
"""
This is the Auth module.

This module is responsible for handling API authentication.
"""

from typing import List, TypeVar
from flask import request

class Auth:
    """
    Auth Class
    
    This class is responsible for managing authentication
    for all your API endpoints.
    """
    
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to require authentication. Returns False for now. """
        return False

    def authorization_header(self, request=None) -> str:
        """ Method to get the authorization header. Returns None for now. """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to get the current user. Returns None for now. """
        return None