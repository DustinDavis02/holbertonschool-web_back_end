#!/usr/bin/env python3
"""This module is designed to obfuscate specific fields in a log message."""


from typing import List
import re

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields.
    
    Parameters:
        fields (List[str]): Fields to be obfuscated.
        redaction (str): String to replace field values.
        message (str): Original log message.
        separator (str): Character that separates each field in the log line.
        
    Returns:
        str: The log message with specified fields obfuscated.
    """
    return re.sub(fr'(?<=\b{separator.join(fields)}=)([^{separator}]*)', redaction, message)

if __name__ == "__main__":
    pass
