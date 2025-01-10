"""
Write me a simple spell checking engine.
The query language is a very simple regular expression-like language, 
with one special character: . (the dot character), which means 
EXACTLY ONE character (it can be any character). So, for example, 
'c.t' would match 'cat' as the dot matches any character. There may be 
any number of dot characters in the query (or none).

Your spell checker will have to be optimized for speed, so you 
will have to write it in the required way. There would be a 
one-time setUp() function that does any pre-processing you require, 
and then there will be an isMatch() function that should run as fast as 
possible, utilizing that pre-processing.

There are some examples below, feel free to ask for clarification.

Word List:

[cat, bat, rat, drat, dart, drab]

Queries:

cat -> true
c.t -> true
.at -> true
..t -> true
d..t -> true
dr.. -> true
... -> true
.... -> true

..... -> false
h.t -> false
c. -> false

// write a function
// Struct setup(List<String> list_of_words)
// Do whatever processing you want here
// with reasonable efficiency.
// Return whatever data structures you want.
// This function will only run once

// write a function
// bool isMatch(Struct struct, String query)
// Returns whether the query is a match in the
// dictionary (True/False)
// Should be optimized for speed
"""


def set_up(word_list):
    pos_map = {}
    for word in word_list:
        for i, char in enumerate(word):
            pos_map[i] = pos_map.get(i, set()).union(char)

    return pos_map


def is_match(pos_map, word_list, query):
    if query not in word_list:
        if query == None or len(query) == 0:
            return False

        lens = set(len(word) for word in word_list)
        if len(query) not in lens:
            return False

        for i, char in enumerate(query):
            if char not in pos_map[i] and char != ".":
                return False

    return True


word_list = ['cat', 'bte', 'art', 'drat', 'dart', 'drab']
pos_map = set_up(word_list)
assert is_match(pos_map, word_list, "cat") == True
assert is_match(pos_map, word_list, "c.t") == True
assert is_match(pos_map, word_list, ".at") == True
assert is_match(pos_map, word_list, "..t") == True
assert is_match(pos_map, word_list, "d..t") == True
assert is_match(pos_map, word_list, "dr..") == True
assert is_match(pos_map, word_list, "...") == True
assert is_match(pos_map, word_list, "....") == True
assert is_match(pos_map, word_list, "") == False
assert is_match(pos_map, word_list, ".....") == False
assert is_match(pos_map, word_list, "h.t") == False
assert is_match(pos_map, word_list, "c.") == False


word_list = []
pos_map = set_up(word_list)
assert is_match(pos_map, word_list, "cat") == False