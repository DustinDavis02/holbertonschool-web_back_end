#!/usr/bin/env python3
"""
This is the session_auth module.
"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ SessionAuth class. """
    def create_session(self, user_id: str = None) -> str:
        """ Creates Session ID for user_id """
        from uuid import uuid4
        if user_id is None or type(user_id) is not str:
            return None
        session_id = str(uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id
