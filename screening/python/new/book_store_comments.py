""" The bookstore gathered a list of customer comments from each shop location 
and wants to find the most common 
comment across all locations (ignoring duplicates from the same location). 
If multiple comments appear the same number of times, return any one of them. """

"""
you are given a dictionary where the key is location of book store and value is the list of reviews as string. 
the list can have duplicate values. return the most frequent review across all 
locations after removing the duplicate review for each location.
"""


def solution(comments):
    count = {}
    for _, v in comments.items():
        for comment in set(v):
            count[comment] = count.get(comment, 0) + 1

    highest = max(count.values())

    ans = [k for k, v in count.items() if v == highest]

    return ans[0]


reviews_by_location = {
    "Location1": ["Great service!", "Loved it", "Great service!"],
    "Location2": ["Loved it", "Great selection", "Loved it"],
    "Location3": ["Great service!", "Great selection", "Amazing books"],
}
assert solution(reviews_by_location) in [
    "Loved it",
    "Great service!",
    "Great selection",
]
