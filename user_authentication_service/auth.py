#!/usr/bin/env python3
"""This module contains utility functions for authentication."""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate user login based on email and password.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8')
                                 , user.hashed_password)
        except NoResultFound:
            return False

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a user with a given email and password.
        """
        try:
            # Check if user exists
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # Hash password
            hashed_password = _hash_password(password)
            # Add user to database
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def create_session(self, email: str) -> str:
        """
        Create a new session for a user.
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str):
        """
        Retrieve the user corresponding to a session ID.
        """
        if session_id is None:
            return None

        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None


def _generate_uuid() -> str:
    """
    Returns a string representation of a new UUID.
    """
    return str(uuid.uuid4())


def _hash_password(password: str) -> bytes:
    """
    Hashes password string and returns salted hash bytes.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
