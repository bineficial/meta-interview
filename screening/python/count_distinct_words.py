"""
Count distinct words in a sentence.
"""

import string


def solution(sent):
    sent = "".join(c for c in sent if c not in set(string.punctuation))

    count = {}
    for word in sent.split():
        count[word] = count.get(word, 0) + 1

    result = [v for k, v in count.items() if v == 1]

    return len(result)


def solution(sentence):
    distinct_words = set(sentence.split())

    return len(distinct_words)


assert solution("") == 0
assert solution("once") == 1
assert solution("once twice") == 2
assert solution("once twice twice") == 1
assert solution("this is a sentence") == 4
