#!/usr/bin/env python3
'''filtered_logger.py'''
import re


def filter_datum(fields, redaction, message, separator):
    '''function called filter_datum that returns the log message'''
    return re.sub(
            fr'({"|".join(fields)})=[^{separator}]*', fr'\1={redaction}',
            message)
