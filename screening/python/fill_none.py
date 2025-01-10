"""
Given an array containing None values fill in the 
None values with most recent non None value in the array.
"""


def solution(nums):
    if nums == None or len(nums) == 0:
        return nums

    prev = None
    res = []
    for i, n in enumerate(nums):
        if n == None:
            res.append(prev)
        else:
            res.append(n)
            prev = n

    return res


assert solution([]) == []
assert solution([None, None, None, None]) == [None, None, None, None]
assert solution([1, None, 2, 3, None, None, 5, None]) == [
    1, 1, 2, 3, 3, 3, 5, 5]
assert solution([12, 34, None, 1, 2, 3, 22, None, 23, 24, 25, None, 25, 17, 29, None, None, 1]) == [
    12, 34, 34, 1, 2, 3, 22, 22, 23, 24, 25, 25, 25, 17, 29, 29, 29, 1]
assert solution([None, 1, 2, 3, None, 4, None, None]) == [
    None, 1, 2, 3, 3, 4, 4, 4]
