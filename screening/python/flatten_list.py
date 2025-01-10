"""
Flatten a list.
"""


def solution(nums):
    result = []

    for n in nums:
        if isinstance(n, list):
            inner_list = solution(n)
            result += inner_list
        else:
            result.append(n)

    return result


assert solution([]) == []
assert solution([[]]) == []
assert solution([1, 2]) == [1, 2]
assert solution([1, [2, 3, 4]]) == [1, 2, 3, 4]
assert solution([1, 2, [3, 4, [5], [6, 7, [8, [9]]]]]) == [
    1, 2, 3, 4, 5, 6, 7, 8, 9]
