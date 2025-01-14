"""
There are many meetings with start and end time. How many meetings can occur at the same time?
"""


def solution(meetings):
    events = []
    for meeting in meetings:
        s, e = meeting
        events.append((s, 1))
        events.append((e, -1))

    events = sorted(events)

    meeting_count = 0
    cur_meeting_count = 0
    for event in events:
        cur_meeting_count += event[1]
        meeting_count = max(meeting_count, cur_meeting_count)

    return meeting_count


# Test case 1: Basic overlapping meetings
assert (
    solution([(1, 10), (2, 12), (14, 15)]) == 2
)  # Max overlap: 2 meetings overlap at times 2-10

# Test case 2: Non-overlapping meetings
assert (
    solution([(1, 5), (6, 10), (11, 15)]) == 1
)  # No overlap, maximum is 1 meeting at a time

# Test case 3: Fully overlapping meetings
assert (
    solution([(1, 5), (2, 4), (3, 5), (2, 5)]) == 4
)  # All meetings overlap at time 2-4

# Test case 4: Meetings with same start and end time
assert (
    solution([(1, 5), (1, 5), (1, 5)]) == 3
)  # All meetings overlap, maximum is 3 meetings at the same time

# Test case 5: Meetings with no overlap at all
assert (
    solution([(1, 2), (3, 4), (5, 6), (7, 8)]) == 1
)  # No overlap, maximum is 1 meeting at a time

# Test case 6: Meetings ending at the same time they start (edge case)
assert (
    solution([(1, 3), (3, 6), (6, 9), (9, 12)]) == 1
)  # Each meeting starts when another ends, maximum is 1

# Test case 7: Meetings that end before others start (non-overlapping)
assert (
    solution([(1, 5), (6, 10), (11, 15), (16, 20)]) == 1
)  # No overlap, maximum is 1 meeting at a time

# Test case 9: Edge case with no meetings
assert solution([]) == 0  # No meetings, so no overlap

# Test case 10: Random meetings with varying overlaps
assert (
    solution([(1, 5), (4, 8), (6, 9), (8, 10), (11, 15)]) == 2
)  # Max overlap occurs at time 6-8 with 3 meetings

# Test case 11: Meetings that are all contained within each other
assert solution([(1, 10), (2, 5), (3, 4)]) == 3  # All meetings overlap at time 3-4
