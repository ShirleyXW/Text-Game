from unittest import TestCase
from subjects import subject_grades


class Test(TestCase):
    def test_subject_grades_2_row_equals_2_column_equals_2(self):
        expected = 2
        actual = subject_grades(2, 2)
        self.assertEqual(expected, actual)

    def test_subject_grades_2_row_equals_2_column_equals_1(self):
        expected = 2
        actual = subject_grades(2, 1)
        self.assertEqual(expected, actual)

    def test_subject_grades_3_row_equals_3_column_equals_3(self):
        expected = 3
        actual = subject_grades(3, 3)
        self.assertEqual(expected, actual)

    def test_subject_grades_3_row_equals_3_column_equals_2(self):
        expected = 3
        actual = subject_grades(3, 3)
        self.assertEqual(expected, actual)

    def test_subject_grades_4_row_equals_4_column_equals_3(self):
        expected = 4
        actual = subject_grades(4, 3)
        self.assertEqual(expected, actual)

    def test_subject_grades_4_row_equals_4_column_equals_2(self):
        expected = 4
        actual = subject_grades(4, 2)
        self.assertEqual(expected, actual)
