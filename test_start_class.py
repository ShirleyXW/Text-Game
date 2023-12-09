import io

from unittest import TestCase
from game import start_class
from map import generate_map
from unittest.mock import patch


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_start_class_in_boss_room(self, _):
        test_map = generate_map()
        test_character = {"location": (4, 4), "user_name": "Alice", "in_question": False}
        actual_result = start_class(test_map, test_character)
        expected_question = ("Hello!!! The last question is"
                             " \"Know your student~\"\n\n"
                             "Please find out who is the author creates this beautiful game?")

        self.assertEqual(actual_result[0], expected_question)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_start_class_in_entrance(self, _):
        test_map = generate_map()
        test_character = {"location": (0, 0), "user_name": "Alice", "in_question": False}
        actual_result = start_class(test_map, test_character)

        self.assertEqual(actual_result, None)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_start_class_in_garden(self, _):
        test_map = generate_map()
        test_character = {"location": (2, 2), "user_name": "Alice", "in_question": False}
        actual_result = start_class(test_map, test_character)

        self.assertEqual(actual_result, None)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_start_class_in_classroom_proceeded_automatically(self, _):
        test_map = generate_map()
        test_character = {"location": (1, 1), "user_name": "Alice", "in_question": False, "intelligence": 100,
                          "experience": 0, "level": 1}
        actual_result = start_class(test_map, test_character)

        self.assertEqual(actual_result, None)
        self.assertEqual(test_character["experience"], 2)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_start_class_in_classroom_answering_question_required(self, _):
        test_map = generate_map()
        test_character = {"location": (1, 1), "user_name": "Alice", "in_question": False, "intelligence": 0,
                          "experience": 0, "level": 1}
        actual_result = start_class(test_map, test_character)

        self.assertNotEqual(actual_result, None)
        self.assertEqual(test_character["experience"], 0)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_start_class_in_classroom_already_completed(self, _):
        test_map = generate_map()
        test_map[(3, 3)]["completed"] = True
        test_character = {"location": (3, 3), "user_name": "Alice", "in_question": False, "intelligence": 0,
                          "experience": 0, "level": 1}
        actual_result = start_class(test_map, test_character)

        self.assertEqual(actual_result, None)
        self.assertEqual(test_character["experience"], 0)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_start_class_in_classroom_already_in_question_class_proceeded_automatically(self, _):
        test_map = generate_map()
        test_character = {"location": (3, 3), "user_name": "Alice", "in_question": True, "intelligence": 100,
                          "experience": 0, "level": 1}
        actual_result = start_class(test_map, test_character)

        self.assertEqual(actual_result, None)
