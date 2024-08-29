#!/usr/bin/env python3
"""
Module for filtering log messages by obfuscating specified fields.
"""

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specific fields in a log message.

    Args:
        fields (List[str]): List of strings representing fields to obfuscate.
        redaction (str): String representing what the field will be obfuscated with.
        message (str): The log message to be filtered.
        separator (str): Character separating fields in the log message.

    Returns:
        str: The filtered log message with specified fields obfuscated.
    """
    pattern = r'({}=).*?({})'.format('|'.join(fields), separator)
    return re.sub(pattern, r'\1{}{}'.format(redaction, separator), message)

