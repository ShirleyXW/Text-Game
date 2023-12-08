from unittest import TestCase
from game import process_automatically
from map import generate_map
import unittest.mock
import io


class Test(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_process_automatically(self, _):
        test_character = {"in_question": True, "user_name": "Shirley", "location": (2, 3), "experience": 0, "level": 1}
        test_map = generate_map()
        expected = ("This time your mastery of the subject captivated the class, and you effectively delivered "
                    "this lesson! Keep trying Shirley\nExperience +2\n")
        process_automatically(test_character, test_map)
        self.assertEqual(expected, _.getvalue())
