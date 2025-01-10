"""
Write a function that takes a number
and return a list of its digits
"""


def solution(n):
    return [int(c) for c in str(n)]


assert solution(0) == [0]
assert solution(123) == [1, 2, 3]
assert solution(400) == [4, 0, 0]
