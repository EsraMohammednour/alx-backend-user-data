#!/usr/bin/env python3
'''filtered_logger.py'''
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''format function'''
        msg = super(RedactingFormatter, self).format(record)
        txt = filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
        return txt


patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}


def filter_datum(
        fields: List[str], redaction: str, message: str,
        separator: str) -> str:
    '''function called filter_datum that returns the log message'''
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)
