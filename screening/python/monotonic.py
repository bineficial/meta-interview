"""
Given an array of integers, we would like to 
determine whether the array is monotonic 
(non-decreasing/non-increasing) or not.
"""


def solution(nums):
    if len(nums) == 0:
        return False

    is_inc = True
    is_dec = True

    for i, n in enumerate(nums[1:]):
        if nums[i] > n:
            is_inc = False
        if nums[i] < n:
            is_dec = False

    return is_inc or is_dec


assert solution([]) == False
assert solution([1]) == True
assert solution([1, 2]) == True
assert solution([1, 2, 1]) == False
assert solution([2, 1]) == True
assert solution([1, 2, 5, 8]) == True
assert solution([9, 4, 4, 2, 2]) == True
assert solution([1, 4, 6, 3]) == False
assert solution([1, 1, 1, 1, 1, 1]) == True
