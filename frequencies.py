"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    items = [str(i) for i in items]
    frequencies = {i:items.count(i) for i in items}
    return frequencies

print(frequencies(['0', 4,4,'4','d','d','e',0,'a','d','4']))