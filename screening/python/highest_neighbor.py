"""
Find the alphabet with highest neighbors
"""


def solution(data):
    count = {}

    for group in data:
        if len(group) == 1:
            count[group[0]] = count.get(group[0], 0) + 0
        else:
            for node in group:
                count[node] = count.get(node, 0) + 1

    highest = max(count.values(), default=-1)

    result = [k for k, v in count.items() if v == highest]

    return result


def solution(data):
    count = {}

    for pair in data:
        if len(pair) == 2:
            a, b = pair[0], pair[1]

            count[a] = count.get(a, 0) + 1
            count[b] = count.get(b, 0) + 1
        elif len(pair) == 1:
            count[pair[0]] = count.get(pair[0], 0)

    ans = []
    highest = max(count.values(), default=-1)
    for k, v in count.items():
        if v == highest:
            ans.append(k)

    return ans


assert solution([]) == []
assert solution([[]]) == []
assert solution([["A"], ["B"]]) == ["A", "B"]
assert solution([["A", "B"]]) == ["A", "B"]
assert solution([["A"], ["A", "B"], ["A", "C"], ["B", "D"], ["C", "A"]]) == ["A"]
