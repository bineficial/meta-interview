"""
Given a list of tuples of movie watched times, find 
how many unique minutes of the movie did the viewer 
watch e.g. [(0,15),(10,25)]. The viewer watched 25 
minutes of the movie.
"""


def solution(times):
    if len(times) == 0:
        return 0

    times = sorted(times)
    total = times[0][1] - times[0][0]

    for i in range(1, len(times)):
        cur = times[i]
        prev = times[i-1]

        if cur[0] >= prev[1]:
            total += cur[1] - cur[0]
        else:
            if cur[1] > prev[1]:
                total += cur[1] - prev[1]

    return total


assert solution([]) == 0
assert solution([(0, 0)]) == 0
assert solution([(0, 5)]) == 5
assert solution([(0, 0), (0, 0)]) == 0
assert solution([(0, 0), (1, 2)]) == 1
assert solution([(0, 10), (15, 25), (12, 20), (30, 48)]) == 41
assert solution([(0, 9), (0, 10), (1, 9)]) == 10
assert solution([(0, 15), (10, 25)]) == 25
