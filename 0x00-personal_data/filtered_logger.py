#!/usr/bin/env python3
'''filtered_logger.py'''
import re


patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}
def filter_datum(fields, redaction, message, separator):
    '''function called filter_datum that returns the log message'''
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)
