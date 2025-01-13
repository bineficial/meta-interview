""" Determine the maximum number of unique books that can be bought, 
given an array of book prices and a budget (each book can be purchased only once) 
"""

def solution(prices, budget):
    count = 0
    cumu_budget = budget
    for price in sorted(prices):
        if price <= cumu_budget:
            cumu_budget = cumu_budget - price
            count += 1

    return count

# Test Case 1: Standard case with a mix of prices
prices = [20, 10, 5, 8, 15, 30]
budget = 40
assert solution(prices, budget) == 4  # Expected: 4 books (5, 8, 10, 15)

# Test Case 2: Budget is too small to buy any book
prices = [20, 15, 30]
budget = 5
assert solution(prices, budget) == 0  # Expected: 0 books

# Test Case 3: Budget allows buying all books
prices = [10, 15, 5]
budget = 50
assert solution(prices, budget) == 3  # Expected: 3 books (all)

# Test Case 4: Exact budget matches the sum of the cheapest books
prices = [10, 20, 5, 8, 7]
budget = 30
assert solution(prices, budget) == 4  # Expected: 4 books (5, 7, 8, 10)

# Test Case 5: Only one book is affordable
prices = [100, 50, 25]
budget = 50
assert solution(prices, budget) == 1  # Expected: 1 book (25)

# Test Case 6: All books cost the same
prices = [10, 10, 10, 10, 10]
budget = 30
assert solution(prices, budget) == 3  # Expected: 3 books (10, 10, 10)

# Test Case 7: Empty price list
prices = []
budget = 50
assert solution(prices, budget) == 0  # Expected: 0 books

# Test Case 8: Budget is zero
prices = [5, 10, 15]
budget = 0
assert solution(prices, budget) == 0  # Expected: 0 books

# Test Case 9: Single book available, exactly matches the budget
prices = [50]
budget = 50
assert solution(prices, budget) == 1  # Expected: 1 book (50)

# Test Case 10: Large input
prices = [i for i in range(1, 101)]  # Prices from 1 to 100
budget = 250
assert solution(prices, budget) == 21  # Expected: Sum of first 22 numbers <= 250

print("All test cases passed!")
