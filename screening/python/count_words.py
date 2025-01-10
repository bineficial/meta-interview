"""
Count the number of times a word appear in a sentence using a Hash Map.
"""
import string

def solution(sent, input_word):
    sent = "".join(c for c in sent if c not in set(string.punctuation))
    
    count = {}
    for word in sent.split():
        count[word] = count.get(word, 0) + 1

    return count.get(input_word, 0)


assert solution("", "") == 0
assert solution("once", "") == 0
assert solution("" ,"once") == 0
assert solution("once", "twice") == 0
assert solution("once twice twice", "twice") == 2
