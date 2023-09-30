"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {str(i):items.count(str(i)) for i in items}
    return frequencies