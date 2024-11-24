#!/usr/bin/env python3
'''module for crating new class'''
from .auth import Auth
import re
import binascii
import base64


class BasicAuth(Auth):
    '''creating empty class'''
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        '''return Base64 authorization header'''
        if isinstance(authorization_header, str):
            pattern = r'Basic (?P<token>.+)'
            field_match = re.fullmatch(pattern, authorization_header.strip())
            if field_match is not None:
                return field_match.group('token')
        return None

    def decode_base64_authorization_header(
                                            self,
                                            base64_authorization_header:
                                            str) -> str:
        '''decode base64 authorization header'''
        if isinstance(base64_authorization_header, str):
            try:
                decoded_bytes = base64.b64decode(
                                base64_authorization_header, validate=True)
                return decoded_bytes.decode('utf-8')

            except (binascii.Error, UnicodeDecodeError):
                return None

    def extract_user_credentials(
                                self,
                                decoded_base64_authorization_header:
                                str) -> (str, str):
        '''Basic - User credentials'''
        if decoded_base64_authorization_header is None:
            return None, None
        elif not isinstance(decoded_base64_authorization_header, str):
            return None, None
        elif ":" not in decoded_base64_authorization_header:
            return None, None
        return decoded_base64_authorization_header.split(':')
