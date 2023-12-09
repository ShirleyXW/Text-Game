from unittest import TestCase
from game import get_character_info


class Test(TestCase):
    def test_get_character_info_name_Alice(self):
        test_character = {
            "user_name": "Alice",
            "health": 1,
            "max_health": 5,
            "level": 2,
            "intelligence": 1,
            "experience": 3
        }
        actual = get_character_info(test_character)
        expected = ("\nCurrent character Alice info:\n"
                    "  Health        1/5\n"
                    "  Level         2\n"
                    "  Intelligence  1\n"
                    "  Experience    3/10\n")
        self.assertEqual(expected, actual)

    def test_get_character_info_name_Bob(self):
        test_character = {
            "user_name": "Bob",
            "health": 1,
            "max_health": 5,
            "level": 2,
            "intelligence": 1,
            "experience": 3
        }
        actual = get_character_info(test_character)
        expected = ("\nCurrent character Bob info:\n"
                    "  Health        1/5\n"
                    "  Level         2\n"
                    "  Intelligence  1\n"
                    "  Experience    3/10\n")
        self.assertEqual(expected, actual)

    def test_get_character_info_health_5(self):
        test_character = {
            "user_name": "Bob",
            "health": 5,
            "max_health": 5,
            "level": 2,
            "intelligence": 1,
            "experience": 3
        }
        actual = get_character_info(test_character)
        expected = ("\nCurrent character Bob info:\n"
                    "  Health        5/5\n"
                    "  Level         2\n"
                    "  Intelligence  1\n"
                    "  Experience    3/10\n")
        self.assertEqual(expected, actual)

    def test_get_character_info_level_3(self):
        test_character = {
            "user_name": "Bob",
            "health": 5,
            "max_health": 5,
            "level": 3,
            "intelligence": 1,
            "experience": 3
        }
        actual = get_character_info(test_character)
        expected = ("\nCurrent character Bob info:\n"
                    "  Health        5/5\n"
                    "  Level         3\n"
                    "  Intelligence  1\n"
                    "  Experience    3/10\n")
        self.assertEqual(expected, actual)

    def test_get_character_info_exp_10(self):
        test_character = {
            "user_name": "Bob",
            "health": 5,
            "max_health": 5,
            "level": 3,
            "intelligence": 1,
            "experience": 10
        }
        actual = get_character_info(test_character)
        expected = ("\nCurrent character Bob info:\n"
                    "  Health        5/5\n"
                    "  Level         3\n"
                    "  Intelligence  1\n"
                    "  Experience    10/10\n")
        self.assertEqual(expected, actual)
