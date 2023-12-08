from unittest import TestCase
from subjects import subjects, SUBJECTS
from unittest.mock import patch


class Test(TestCase):
    @patch("random.randint", side_effect=[0])
    def test_subject_is_science(self, _):
        expected = SUBJECTS[0]
        actual = subjects()
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[1])
    def test_subject_is_geography(self, _):
        expected = SUBJECTS[1]
        actual = subjects()
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[2])
    def test_subject_is_computer(self, _):
        expected = SUBJECTS[2]
        actual = subjects()
        self.assertEqual(expected, actual)
