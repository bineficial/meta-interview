"""
Remove duplicates from a list.
"""


def solution(a_list):
    seen = set()
    result = []

    for e in a_list:
        if e not in seen:
            result.append(e)
        seen.add(e)

    return result


assert solution([]) == []
assert solution([1, 1, 2, 1, 1]) == [1, 2]
