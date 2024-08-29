#!/usr/bin/env python3
"""
This module provides a function to obfuscate specific fields in log messages.
"""

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Replace specified fields in the log message with a redaction string.

    Args:
        fields (List[str]): A list of field names to obfuscate.
        redaction (str): The string to replace the field values with.
        message (str): The log message to process.
        separator (str): The character that separates fields in the log message.

    Returns:
        str: The obfuscated log message.
    """
    return re.sub(r'(?<=' + separator + '|^)(?:' + '|'.join(fields) + r')=[^' + separator + r']*', lambda m: f"{m.group(0).split('=')[0]}={redaction}", message) + '\n'

