"""
Given a list of tuples of movie watched times, find 
how many unique minutes of the movie did the viewer 
watch e.g. [(0,15),(10,25)]. The viewer watched 25 
minutes of the movie.
"""


def solution(times):
    times = sorted(times)

    prev = (0, 0)
    total = 0

    for time in times:
        s, e = time

        if s >= prev[1]:
            total += e - s
            prev = time
        elif s < prev[1] and e > prev[1]:
            total += e - prev[1]
            prev = time

    return total


assert solution([]) == 0
assert solution([(0, 0)]) == 0
assert solution([(0, 5)]) == 5
assert solution([(0, 0), (0, 0)]) == 0
assert solution([(0, 0), (1, 2)]) == 1
assert solution([(0, 10), (15, 25), (12, 20), (30, 48)]) == 41
assert solution([(0, 9), (0, 10), (1, 9), (1, 10), (2, 12)]) == 12
assert solution([(0, 15), (10, 25)]) == 25
