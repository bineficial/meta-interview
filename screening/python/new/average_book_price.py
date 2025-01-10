""" Calculate the average book price from a list of prices """


def solution(prices):
    return sum(prices) / len(prices)


assert solution([]) == 0
assert solution([10]) == 10
assert solution([10, 20, 30]) == 20
assert solution([5, 15, 25, 35]) == 20
