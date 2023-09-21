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

    class is responsible for managing authentication
    for all API endpoints.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method to require authentication based on the path and excluded_paths.

        Parameters:
            - path (str): The path from the request
            - excluded_paths (List[str]): List of string paths that don't need authentication

        Returns:
            bool: True if authentication is required, False if not
        """
    
        # Case 1: path is None
        if path is None:
            return True

        # Case 2: excluded_paths is None or empty
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Make method slash-tolerant
        path = path.rstrip('/')

        # Case 3: path is in excluded_paths
        return not any(ex_path.rstrip('/')
                       == path for ex_path in excluded_paths)

    def authorization_header(self, request=None) -> str:
        """ Method to get the authorization header. Returns None for now. """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to get the current user. Returns None for now. """
        return None
