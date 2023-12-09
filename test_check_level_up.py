from unittest import TestCase
from game import check_level_up
import io
from unittest.mock import patch


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_max_level(self, _):
        test_character = {
            "user_name": "Alice",
            "health": 1,
            "max_health": 5,
            "level": 3,
            "intelligence": 1,
            "experience": 0
        }
        check_level_up(test_character)
        expected = False
        self.assertEqual(expected, check_level_up(test_character))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_insufficient_exp(self, _):
        test_character = {
            "user_name": "Alice",
            "health": 1,
            "max_health": 5,
            "level": 3,
            "intelligence": 1,
            "experience": 8
        }
        check_level_up(test_character)
        expected = False
        self.assertEqual(expected, check_level_up(test_character))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_2(self, _):
        test_character = {
            "user_name": "Alice",
            "health": 1,
            "max_health": 5,
            "level": 1,
            "intelligence": 1,
            "experience": 11
        }
        check_level_up(test_character)
        expected = ("You leveled up! Your intelligence +3.\n"
                    "\nCurrent character Alice info:\n"
                    "  Health        1/5\n"
                    "  Level         2\n"
                    "  Intelligence  4\n"
                    "  Experience    1/10\n\n")
        self.assertEqual(expected, _.getvalue())
