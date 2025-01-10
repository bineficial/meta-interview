# Facebook Data Engineer Interview Questions

## Technical Screening

### Python

---

#### Given a two dimensional list, for example [ [2,3],[3,4],[5]] person 2 is friends with 3 etc, find how many friends each person has. Note, one person has no friends.
```py
def solution(data):
    counts = {}

    for friend_group in data:
        if len(friend_group) == 1:
            counts[friend_group[0]] = 0
        else:
            for person in friend_group:
                counts[person] = counts.get(person, 0) + 1

    return counts

assert count_friends([[2,3],[3,4],[5]]) == {2: 1, 3: 2, 4: 1, 5: 0}
```

## Mission Statement
To give people the power to build community and bring the world closer together