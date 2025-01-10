"""
Given a number and an array find the sum of any 2 numbers in a list is equal to a given number.
"""


def solution(nums, target):
    hm = {}

    for i, n in enumerate(nums):
        diff = target - n

        if n in hm:
            return [hm[n], i]
        else:
            hm[diff] = i


assert solution([2, 7, 11, 15], 9) == [0, 1]
assert solution([3, 2, 4], 6) == [1, 2]
assert solution([3, 3], 6) == [0, 1]
