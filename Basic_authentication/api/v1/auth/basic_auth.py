#!/usr/bin/env python3
"""
This is the BasicAuth module.

This module is responsible for handling Basic API authentication.
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth Class

    class is responsible for handling Basic authentication
    for all API endpoints.
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str)-> str:
        """
        Extracts the Base64 encoded part of the authorization header.

        Parameters:
            authorization_header (str): Authorization header value.

        Returns:
            str: Base64 encoded part, the Authorization header if valid,
            otherwise None.
        """

        # Check if authorization_header is there or not
        if authorization_header is None:
            return None

        # Check if authorization_header is anything but a string
        if not isinstance(authorization_header, str):
            return None

        # Check if authorization_header doesn't start with "Basic"
        if not authorization_header.startswith("Basic "):
            return None

        # Extract and return the Base64 encoded part
        return authorization_header.split(" ")[1]
