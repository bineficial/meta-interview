"""
Write a function that returns the cumulative
sum of elements in a list.
"""


def solution(nums):
    prev = 0
    result = []
    for n in nums:
        prev = n + prev
        result.append(prev)
    return result


assert solution([]) == []
assert solution([0, 0]) == [0, 0]
assert solution([1, 1, 1]) == [1, 2, 3]
assert solution([1, -1, 3]) == [1, 0, 3]
assert solution([100, -1, 5]) == [100, 99, 104]
