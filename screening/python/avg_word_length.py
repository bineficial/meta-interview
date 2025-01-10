"""
Calculate the average word length.
"""
import string

def solution(sent):
    sent = "".join(c for c in sent if c not in set(string.punctuation))

    words = sent.split()
    len_total = sum(len(word) for word in words)
    len_words = len(words)
    return len_total / len_words if len_words else 0


assert solution("") == 0
assert solution("Hi my name is Bob") == 2.6
assert solution("Hi, my name is Bob") == 2.6
assert solution("4444 4444") == 4.0
