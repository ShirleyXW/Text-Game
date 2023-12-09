from unittest import TestCase
from game import loose_health
from unittest.mock import patch
import io


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_loose_health_minus_3(self, _):
        loose_health({"user_name": "Alice", "location": (1, 1), "in_question": True, "health": 10}, 3)
        expected = "Health -3.\n"
        self.assertEqual(expected, _.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_loose_health_minus_1(self, _):
        test_character = {"user_name": "Alice", "location": (1, 1), "in_question": True, "health": 10}
        loose_health(test_character, 1)
        expected = "Health -1.\n"
        expected_health = 9
        actual_health = test_character["health"]
        self.assertEqual(expected, _.getvalue())
        self.assertEqual(expected_health, actual_health)
