""" You have have a number with multiple digits - you need to construct the largest possible number from these digits. """

def solution(num):
    ans = "".join(sorted(list(str(num)), reverse=True))

    return int(ans)

assert solution(123) == 321