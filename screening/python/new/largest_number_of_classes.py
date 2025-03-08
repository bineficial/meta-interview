from dataclasses import dataclass

"""
Given a list of workshops, return the largest number of classes
that were hosted in total across any consecutive years that had
at least one workshop each.
"""


@dataclass()
class Workshop:
    name: str
    classes_per_year: int
    start: int
    end: int


def largest_number_of_classes(workshops):
    year_class_count = {}

    for workshop in workshops:
        for year in range(workshop.start, workshop.end + 1):
            year_class_count[year] = (
                year_class_count.get(year, 0) + workshop.classes_per_year
            )

    years = sorted(year_class_count.keys())
    max_classes = 0
    for year in years:
        if year + 1 in years:
            max_classes = max(
                max_classes, year_class_count[year] + year_class_count[year + 1]
            )

    return max_classes


input_1 = [
    Workshop(name="A", classes_per_year=4, start=2000, end=2003),
    Workshop(name="B", classes_per_year=1, start=2001, end=2004),
    Workshop(name="C", classes_per_year=12, start=2004, end=2006),
]
assert largest_number_of_classes(input_1) == 25

input_2 = [
    Workshop(name="A", classes_per_year=13, start=2001, end=2010),
    Workshop(name="B", classes_per_year=4, start=2016, end=2020),
    Workshop(name="C", classes_per_year=2, start=2019, end=2020),
    Workshop(name="C", classes_per_year=52, start=2014, end=2018),
    Workshop(name="C", classes_per_year=1, start=2015, end=2015),
]
assert largest_number_of_classes(input_2) == 112

input_3 = [
    Workshop(name="A", classes_per_year=18, start=2011, end=2015),
    Workshop(name="B", classes_per_year=17, start=2017, end=2020),
    Workshop(name="C", classes_per_year=60, start=2021, end=2022),
]
assert largest_number_of_classes(input_3) == 120
