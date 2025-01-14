"""
Count the number of times a substring appear in a string.
"""


def solution(string, sub_str):
    if sub_str == "":
        return 0

    n, m = len(string), len(sub_str)
    count = 0

    for i in range(n - m + 1):
        if sub_str == string[i : i + m]:
            count += 1

    return count


assert solution("", "") == 0
assert solution("ab", "") == 0
assert solution("", "ab") == 0
assert solution("abaabba", "aba") == 1
assert solution("ababab", "ab") == 3
assert solution("aaaaaa", "aa") == 5
assert solution("azcbobobegghaklbob", "bob") == 3
