""" Given a list of workshops, return the largest number of classes that were hosted in total across any 2 consecutive years that had at least one workshop each. """


def solution(workshops):

    year_to_workshops = {}
    for workshop in workshops:
        year_to_workshops[workshop[0]] = workshop[1]

    max_con_workshops = 0
    for year, num in year_to_workshops.items():
        cur_max_workshops = num + year_to_workshops.get(year + 1, 0)
        max_con_workshops = max(max_con_workshops, cur_max_workshops)

    return max_con_workshops


assert solution([(2020, 10), (2021, 15), (2022, 5), (2023, 20)]) == 25
assert solution([(2020, 10), (2021, 30), (2022, 5)]) == 40
