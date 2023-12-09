from unittest import TestCase
from game import gain_experience
import io
import unittest.mock


class Test(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_gain_experience_but_not_level_up(self, _):
        test_character = {
            "user_name": "Alice",
            "health": 1,
            "max_health": 5,
            "level": 2,
            "intelligence": 1,
            "experience": 0
        }
        gain_experience(test_character)
        expected = "Experience +2\n"
        self.assertEqual(expected, _.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_gain_experience_and_level_up(self, _):
        test_character = {
            "user_name": "Alice",
            "health": 1,
            "max_health": 5,
            "level": 2,
            "intelligence": 1,
            "experience": 8
        }
        gain_experience(test_character)
        expected = ("Experience +2\n"
                    "You leveled up! Your intelligence +3.\n"
                    "\nCurrent character Alice info:\n"
                    "  Health        1/5\n"
                    "  Level         3\n"
                    "  Intelligence  4\n"
                    "  Experience    0/10\n\n")
        self.assertEqual(expected, _.getvalue())
