#!/usr/bin/env python3
"""defines the User class which is a SQLAlchemy model for the users table."""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    defines a table 'users' with the following attributes:
    - id: integer primary key.
    - email: A non-nullable string for the email.
    - hashed_password: A non-nullable string for the hashed password.
    - session_id: A nullable string for the session ID.
    - reset_token: A nullable string for the reset token.
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))
