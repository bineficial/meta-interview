"""
Find common words in 2 sentences
"""


def solution(sent1, sent2):
    words1 = set(sent1.split())
    words2 = set(sent2.split())

    return words1 & words2


assert solution("", "") == set()
assert solution("word", "word") == {"word"}
assert solution("", "word") == set()
assert solution(
    "Firstly this is the first string",
    "Next is the second string"
) == {'string', 'is', 'the'}
