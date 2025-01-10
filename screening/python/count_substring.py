"""
Count the number of times a substring appear in a string.
"""


def solution(string, sub_str):
    len_sub = len(sub_str)
    if len_sub == 0:
        return 0

    count = 0

    for i in range(len(string) - len_sub + 1):
        if sub_str == string[i:i+len_sub]:
            count += 1

    return count


assert solution("", "") == 0
assert solution("ab", "") == 0
assert solution("", "ab") == 0
assert solution("abaabba", "aba") == 1
assert solution("ababab", "ab") == 3
assert solution("aaaaaa", "aa") == 5
assert solution("azcbobobegghaklbob", "bob") == 3
