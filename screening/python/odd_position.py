"""
Write a function that returns the elements
on odd positions (0 based) in a list.
"""


def solution(nums):
    result = []
    for i, n in enumerate(nums):
        if i % 2 != 0:
            result.append(n)

    return result


assert solution([1]) == []
assert solution([]) == []
assert solution([1, 2]) == [2]
assert solution([0, 1, 2, 3, 4, 5]) == [1, 3, 5]
assert solution([1, -1, 2, -2]) == [-1, -2]
