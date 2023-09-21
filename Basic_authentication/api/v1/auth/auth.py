#!/usr/bin/env python3
from typing import List, TypeVar
from flask import request

class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to require authentication. Returns False for now. """
        return False

    def authorization_header(self, request=None) -> str:
        """ Method to get the authorization header. Returns None for now. """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to get the current user. Returns None for now. """
        return None
