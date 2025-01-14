""" Having a dictionary with a list of words, find the word with the most appearings among all of them. """

""" Write a python function which gets a dict of location, list of cities, and returns the name of the city that appears the most times """


def solution(word_dict):
    count = {}
    for _, v in word_dict.items():
        for word in v:
            count[word] = count.get(word, 0) + 1

    max_word = None
    max_count = 0
    for word, count in count.items():
        if count > max_count:
            max_count = count
            max_word = word

    return max_word


word_dict = {
    "list1": ["apple", "banana", "apple", "orange"],
    "list2": ["banana", "orange", "apple", "banana"],
    "list3": ["grape", "apple", "banana", "banana"],
}
assert solution(word_dict) == "banana"

# Test Case 2: Tie between multiple words
word_dict = {
    "list1": ["cat", "dog", "fish"],
    "list2": ["dog", "cat", "fish"],
    "list3": ["fish", "dog", "cat"],
}
result = solution(word_dict)
assert result in ["cat", "dog", "fish"]  # Any word with 3 appearances is valid

# Test Case 3: Single list in the dictionary
word_dict = {
    "list1": ["red", "blue", "blue", "green", "red", "red"],
}
assert solution(word_dict) == "red"

# Test Case 4: Empty dictionary
word_dict = {}
assert solution(word_dict) == None

# Test Case 5: Empty lists in the dictionary
word_dict = {
    "list1": [],
    "list2": [],
    "list3": [],
}
assert solution(word_dict) == None

# Test Case 6: One word appearing in all lists
word_dict = {
    "list1": ["hello"],
    "list2": ["hello"],
    "list3": ["hello", "world"],
}
assert solution(word_dict) == "hello"

# Test Case 7: Large input with multiple repetitions
word_dict = {
    "list1": ["a"] * 100,
    "list2": ["b"] * 50 + ["a"] * 30,
    "list3": ["c"] * 40 + ["b"] * 20 + ["a"] * 10,
}
assert solution(word_dict) == "a"

# Test Case 8: Dictionary with only one key-value pair
word_dict = {
    "list1": ["single", "word", "test", "test"],
}
assert solution(word_dict) == "test"

# Edge Case 1: Case sensitivity
word_dict = {
    "list1": ["apple", "Apple", "APPLE"],
}
result = solution(word_dict)
assert result in ["apple", "Apple", "APPLE"]  # Case-sensitive check

# Edge Case 2: Non-string elements
word_dict = {
    "list1": [1, 2, 2, 3],
    "list2": [3, 3, 1],
}
assert solution(word_dict) == 3  # Integers are allowed
