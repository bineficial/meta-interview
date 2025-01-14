"""
Given an ip address as an input string, validate it and return True/False
"""


def solution(ip):
    parts = ip.split(".")

    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False

        if int(part) < 0 or int(part) > 255:
            return False

        if part != "0" and part[0] == "0":
            return False

    return True


assert solution("") == False
assert solution("....") == False
assert solution("172162541") == False
assert solution("172.16.254.1") == True
assert solution("172.16.254.1.1") == False
assert solution("172.16.254") == False
assert solution("a.16.254.1") == False
assert solution("172.16.256.1") == False
