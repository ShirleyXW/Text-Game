import random

SCIENCE = ("Science", "Sci")
GEOGRAPHY = ("Geography", "Geo")
COMPUTER_SCIENCE = ("Computer Science", "C&S")
SUBJECTS = (SCIENCE, GEOGRAPHY, COMPUTER_SCIENCE)


def subjects():
    subject = SUBJECTS[random.randint(0, 2)]
    return subject


def subject_grades(row, column):
    if row <= 2 and column <= 2:
        return 2
    elif row <= 3 and column <= 3:
        return 3
    else:
        return 4
