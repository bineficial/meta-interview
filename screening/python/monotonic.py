"""
Given an array of integers, we would like to 
determine whether the array is monotonic 
(non-decreasing/non-increasing) or not.
"""


def solution(nums):
    if len(nums) <= 1:
        return True

    is_inc = True
    is_dec = True

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            is_inc = False

        if nums[i] > nums[i - 1]:
            is_dec = False

    return is_inc or is_dec


assert solution([]) == True
assert solution([1]) == True
assert solution([1, 2]) == True
assert solution([1, 2, 1]) == False
assert solution([2, 1]) == True
assert solution([1, 2, 5, 8]) == True
assert solution([9, 4, 4, 2, 2]) == True
assert solution([1, 4, 6, 3]) == False
assert solution([1, 1, 1, 1, 1, 1]) == True
