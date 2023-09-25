#!/usr/bin/env python3
"""
This is the BasicAuth module.

This module is responsible for handling Basic API authentication.
"""

import base64
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """
    BasicAuth Class

    class is responsible for handling Basic authentication
    for all API endpoints.
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                               str) -> str:
        """
        Decodes Base64 encoded part of the authorization header.

        Parameters:
            base64_authorization_header (str): Base64 encoded part of the
            Authorization header.

        Returns:
            str: Decoded Base64 string as UTF8 if valid, otherwise None.
        """

        # Check base64_authorization_header is None
        if base64_authorization_header is None:
            return None

        # Check base64_authorization_header is not a string
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            # Decode Base64 string and return as UTF8
            return base64.b64decode(
                base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self,
        decoded_base64_authorization_header: str
    ) -> (str, str):

        """
        Extracts user email and password from the decoded Base64.

        Parameters:
            decoded_base64_authorization_header (str): The decoded
            string.

        Returns:
            tuple: User email and password if valid, otherwise None.
        """

        # Check decoded_base64_authorization_header is None
        if decoded_base64_authorization_header is None:
            return None, None

        # Check decoded_base64_authorization_header is not a string
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        # Check decoded_base64_authorization_header doesn't contain ':'
        if ':' not in decoded_base64_authorization_header:
            return None, None

        # Extract and return the user email and password
        user_email, user_password = \
            decoded_base64_authorization_header.split(':', 1)
        return user_email, user_password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Returns the User instance based on email and password """
        if (user_email is None or type(user_email) is not str or
                user_pwd is None or type(user_pwd) is not str):
            return None

        try:
            # Try fetching users w/ provided email
            users = User.search({'email': user_email})

            # Check if any user was found w/ given email
            if not users:
                return None

            # Assuming the email is unique and we get a single user back
            user = users[0]

            # Verify password for fetched user
            if not user.is_valid_password(user_pwd):
                return None
        except Exception:
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves the User instance for a request """

        # 1. Get the Authorization header
        auth_header = self.authorization_header(request)
        if not auth_header:
            return None

        # 2. Extract the Base64 part of the Authorization header
        base64_header = self.extract_base64_authorization_header(auth_header)
        if not base64_header:
            return None

        # 3. Decode the Base64 string
        decoded_header = self.decode_base64_authorization_header(
            base64_header)
        if not decoded_header:
            return None

        # 4. Extract user email and password from the decoded string
        user_email, user_pwd = self.extract_user_credentials(decoded_header)
        if not user_email or not user_pwd:
            return None

        # 5. Fetch the User object using the email and password
        user = self.user_object_from_credentials(user_email, user_pwd)
        return user