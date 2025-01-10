"""
Complete a function that returns the number of times a given character occurs in the given string.
"""


def solution(a_str, char):
    if len(char) == 0:
        return 0
    return a_str.count(char)


assert solution("", "") == 0
assert solution("", "s") == 0
assert solution("mississippi", "") == 0
assert solution("mississippi", "s") == 4
