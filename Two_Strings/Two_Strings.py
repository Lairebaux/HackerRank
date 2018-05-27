"""
Given two strings, determine if they share a common substring. A substring may be as small
as one character.
"""

def two_strings(s1, s2):
    sub1, sub2 = set(s1), set(s2)
    if sub1 & sub2:
        return "YES"
    return "NO"

