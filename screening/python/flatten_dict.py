"""
Flatten a nested dictionary.
"""


def solution(data):
    result = {}

    for key, val in data.items():
        if isinstance(val, dict):
            flattened = solution(val)
            for key2, val2 in flattened.items():
                result[key + "_" + key2] = val2
        else:
            result[key] = val

    return result

assert solution({}) == {}
assert solution({"a": 1}) == {"a": 1}
assert solution({"a": 1, "b": {"b2": 2}}) == {"a": 1, "b_b2": 2}
assert solution({"a": {"a2": 2, "a3": 3}}) == {"a_a2": 2, "a_a3": 3}
assert solution({"a": {"a2": {"a3": 3}}}) == {"a_a2_a3": 3}


# If solution requires nesting of lists.
# def solution2(data):
#     result = {}
    
#     for key, val in data.items():
#         if isinstance(val, dict):
#             flattened = solution2(val)

#             for key2, val2 in flattened.items():
#                 result[key + "_" + key2] = val2

#         elif isinstance(val, list):
#             for i, subdict in enumerate(val):
#                 flattened = solution2(subdict)

#                 for key2, val2 in flattened.items():
#                     result[f"{key}_{key2}_{str(i)}"] = val2
#         else:
#             result[key] = val

#     return result

# assert solution2({"a": 1, "b": {"b2": 2}}) == {"a": 1, "b_b2": 2}
# assert solution2({"a": {"a2": 2, "a3": 3}}) == {"a_a2": 2, "a_a3": 3}
# assert solution2({"a": {"a2": {"a3": 3}}}) == {"a_a2_a3": 3}
# assert solution2({"a": [{"b": 1}, {"b": 2}]}) == {'a_b_0': 1, 'a_b_1': 2}