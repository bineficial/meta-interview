""" search an element in an unsorted list """

def solution(items, target):
    for i, item in enumerate(items):
        if item == target:
            return i
        
    return -1

assert solution([1, 3, 2], 3) == 1