"""
Write a function that reutns the smallest nonnegative number which can be
generatred by using all the digits with odd values of a given number.

Example: 10430
Result: 13
"""


def rearrange_digits(number: int):
    new_number = []

    num_str = str(number)
    for n in num_str:
        if n.isdigit():
            if int(n) % 2 != 0:
                new_number.append(int(n))

    new_number = sorted(new_number)
    new_number = "".join([str(n) for n in new_number])

    if new_number == "":
        return None
    else:
        return int(new_number)


assert rearrange_digits(690321) == 139
assert rearrange_digits(10430) == 13
assert rearrange_digits(2024) == None
assert rearrange_digits(0) == None
assert rearrange_digits(-2) == None
assert rearrange_digits(-3) == 3
assert rearrange_digits(-58) == 5
assert rearrange_digits(-79) == 79
assert rearrange_digits(-1717) == 1177
print("Passed!")
