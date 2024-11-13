#!/usr/bin/env python3
'''module for crating new class'''
from .auth import Auth
import re


class BasicAuth(Auth):
    '''creating empty class'''
    def extract_base64_authorization_header(self, authorization_header: str)
    -> str:
        '''return Base64 authorization header'''
        if isunstance(authorization_header, str):
            pattern = r'Basic (?P<token>.+)'
            field_match = re.fullmatch(pattern, authorization_header.strip())
            if field_match is not None:
                return field_match.group('token')
        return None
