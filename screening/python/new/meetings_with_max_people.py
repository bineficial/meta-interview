""" 
You have a list of data classes. The data class represent an object with various start and end time of a meeting as well as 
number of people in the meeting. There are overlapping meetings. Your task Is to find the most number of people that were in a meeting at once.
Meaning total number of people in meatings at any give time.
"""


def solution(meetings):
    events = []

    for meeting in meetings:
        s, e, p = meeting

        events.append((s, p))
        events.append((e, -p))

    events = sorted(events)

    cur_num_people = 0
    max_tot_people = 0

    for event in events:
        cur_num_people += event[1]
        max_tot_people = max(max_tot_people, cur_num_people)

    return max_tot_people


# Test case 1: All meetings overlap
meetings = [
    (1, 5, 10),
    (2, 6, 15),
    (4, 8, 5),
    (7, 9, 10),
]
assert solution(meetings) == 30  # Maximum overlap at time 4-5

# Test case 2: No meetings overlap
meetings = [
    (1, 5, 10),
    (6, 10, 20),
    (11, 15, 30),
]
assert solution(meetings) == 30  # Each meeting occurs independently

# Test case 3: Partially overlapping meetings
meetings = [
    (1, 4, 10),
    (3, 6, 15),
    (5, 8, 20),
]
assert solution(meetings) == 35  # Maximum overlap at time 5-6

# Test case 4: Single meeting
meetings = [
    (1, 10, 50),
]
assert solution(meetings) == 50  # Only one meeting

# Test case 5: Edge case - empty list
meetings = []
assert solution(meetings) == 0  # No meetings

# Test case 6: Meetings with the same start and end times
meetings = [
    (1, 5, 10),
    (1, 5, 15),
    (1, 5, 20),
]
assert solution(meetings) == 45  # All meetings overlap completely

# Test case 7: Non-overlapping followed by overlapping
meetings = [
    (1, 5, 10),
    (6, 10, 20),
    (8, 12, 15),
]
assert solution(meetings) == 35  # Overlap between 8-10

# Test case 8: Meetings with zero participants
meetings = [
    (1, 5, 0),
    (2, 6, 0),
    (4, 8, 0),
]
assert solution(meetings) == 0  # No participants

# Test case 9: Long duration meeting with multiple overlaps
meetings = [
    (1, 100, 50),
    (20, 40, 30),
    (30, 50, 20),
    (60, 80, 25),
]
assert solution(meetings) == 100  # Maximum overlap at time 30-40

# Test case 10: Overlap with large number of participants
meetings = [
    (1, 10, 100),
    (5, 15, 200),
    (10, 20, 300),
]
assert solution(meetings) == 500  # Maximum overlap at time 10-15
