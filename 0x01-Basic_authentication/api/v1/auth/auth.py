#!/usr/bin/env python3
'''manage the API authentication'''
from flask import request
from typing import List, TypeVar
User = TypeVar('User')


class Auth:
    '''class the mange API authentication'''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''Method to check if a given path requires authentication
        '''
        if path is None:
            return True
        elif excluded_paths is None or len(excluded_paths) == 0:
            return True
        for excluded_path in excluded_paths:
            if path.rstrip('/') == excluded_path.rstrip('/'):
                return False
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        ''' return None request'''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''return None request'''
        return None
