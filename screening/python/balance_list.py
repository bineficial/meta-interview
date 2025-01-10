"""
Balance a list of ints, so that each int
has an equal number of appearance in the list.
Return a dictionary that defines the count
of each needed to balance the list.
"""


def solution(nums):
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1

    highest = max(counts.values())

    return {
        k: highest-v
        for k, v in counts.items()
        if highest-v != 0
    }


assert solution([1, 1, 2]) == {2: 1}
assert solution([1, 1, 1, 2, 5, 5]) == {2: 2, 5: 1}
