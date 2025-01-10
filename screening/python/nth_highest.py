"""
Given a dictionary, print the key for nth highest 
value present in the dict. If there are more than 
1 record present for nth highest value then sort 
the key and print the first one.
"""


def solution(data, n):
    if n == 0:
        return None

    a_dict = {}
    for k, v in data.items():
        a_dict[v] = a_dict.get(v, []) + [k]

    highest = sorted(a_dict.keys(), reverse=True)
    if len(highest) >= n:
        nth_highest = highest[n-1]
        key = sorted(a_dict[nth_highest])[0]
        return key
    else:
        return None


assert solution({}, 0) == None
assert solution({}, 1) == None
assert solution({'a': 1}, 1) == 'a'
assert solution({'a': 1}, 2) == None
assert solution({'a': 1, 'b': 2}, 1) == 'b'
assert solution({'a': 1, 'b': 2}, 2) == 'a'
assert solution({'a': 1, 'b': 2, 'c': 2}, 1) == 'b'
assert solution({'a': 1, 'b': 2, 'c': 2, 'd': 1}, 2) == 'a'
assert solution({'a': 1, 'b': 2, 'c': 3}, 3) == 'a'
