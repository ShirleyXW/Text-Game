import random

SCIENCE = ("Science", "Sci")
GEOGRAPHY = ("Geography", "Geo")
COMPUTER_SCIENCE = ("Computer Science", "C&S")
SUBJECTS = (SCIENCE, GEOGRAPHY, COMPUTER_SCIENCE)


def subjects():
    """
    Returns a random subject from the SUBJECTS list

    :precondition: None
    :postcondition: Returns a string representing a randomly selected subject from the list of subjects
    :return: A random subject from the list of subjects

    >>> subjects() in SUBJECTS
    True
    >>> subjects() in SUBJECTS
    True
    """
    subject = SUBJECTS[random.randint(0, 2)]
    return subject


def subject_grades(row, column):
    """
    Determine the subject grade based on the provided row and column coordinates in the school map

    The function divides the school map into three regions based on row and column coordinates:
    - If both the row and column are less than or equal to 2, the subject grade is 2
    - If either the row or column is less than or equal to 3, the subject grade is 3
    - Otherwise, the subject grade is 4

    :param row: The row coordinate in the school map
    :param column: The column coordinate in the school map
    :precondition: `row` and `column` must be integers representing valid coordinates in the school map
    :postcondition: Determines and returns the subject grade based on the provided coordinates
    :return: An integer representing the subject grade (2, 3, or 4)

    >>> subject_grades(1, 1)
    2
    >>> subject_grades(2, 3)
    3
    >>> subject_grades(4, 4)
    4
    """
    if row <= 2 and column <= 2:
        return 2
    elif row <= 3 and column <= 3:
        return 3
    else:
        return 4
