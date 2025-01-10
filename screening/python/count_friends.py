"""
Given a two dimensional list, for example [[2,3],[3,4],[5]] 
person 2 is friends with 3 etc, find how many friends each person has. 
Note, one person has no friends.

You have a 2-D array of friends like [[A,B],[A,C],[B,D],[B,C],[R,M],[S],[P],[A]]. 
Write a function that creates a dictionary of how many friends each person has. 
People can have 0 to many friends. However, there won't be repeat relationships 
like [A,B] and [B,A] and neither will there be more than 2 people in a relationship.

Count the neighbors of each node in a graph. Input graph is a multi dimensional list.
"""


def solution(data):
    counts = {}

    for friend_group in data:
        for person in friend_group:
            if len(friend_group) == 1:
                counts[person] = counts.get(person, 0) + 0
            else:
                counts[person] = counts.get(person, 0) + 1

    return counts


def solution(data):
    """if there is repeating data relationship"""
    relat = {}
    for pair in data:

        if len(pair) == 2:
            a = pair[0]
            b = pair[1]

            relat[a] = relat.get(a, set()) | {b}
            relat[b] = relat.get(b, set()) | {a}
        elif len(pair) == 1:
            relat[pair[0]] = relat.get(pair[0], set()) | set()

    solut = {k: len(v) for k, v in relat.items()}

    return solut


assert solution([]) == {}
assert solution([[]]) == {}
assert solution([[2, 3], [3, 4], [5]]) == {2: 1, 3: 2, 4: 1, 5: 0}
assert solution(
    [["A", "B"], ["B", "C"], ["B", "D"], ["E"]],
) == {"A": 1, "B": 3, "C": 1, "D": 1, "E": 0}
assert solution(
    [["A", "B"], ["A", "C"], ["B", "D"], ["B", "C"], ["R", "M"], ["S"], ["P"], ["A"]]
) == {
    "A": 2,
    "B": 3,
    "C": 2,
    "D": 1,
    "R": 1,
    "M": 1,
    "S": 0,
    "P": 0,
}
