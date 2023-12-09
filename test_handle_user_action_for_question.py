from unittest import TestCase
from game import handle_user_action_for_question
from map import generate_map
from unittest.mock import patch
import io


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_action_invalid(self, _):
        test_map = generate_map()
        test_character = {"user_name": "Alice", "location": (1, 1), "in_question": True, "health": 10}
        question = (
          "What is the capital of France?", ({'A': 'London', 'B': 'Berlin', 'C': 'Madrid', 'D': 'Paris'}, 'd'))
        handle_user_action_for_question(test_map, test_character, question, "e")
        expected = ("Alice, invalid answer. Choose again.\n"
                    "What is the capital of France?\n "
                    "A : London\n "
                    "B : Berlin\n "
                    "C : Madrid\n "
                    "D : Paris\n")
        self.assertEqual(expected, _.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_action_valid_correct_answer(self, _):
        test_map = generate_map()
        test_character = {
            "user_name": "Alice",
            "location": (3, 4),
            "in_question": True,
            "health": 10,
            "experience": 2,
            "level": 1
        }
        question = (
            "What is the capital of France?", ({'A': 'London', 'B': 'Berlin', 'C': 'Madrid', 'D': 'Paris'}, 'd'))
        handle_user_action_for_question(test_map, test_character, question, "d")
        expected = "Correct! Good job, Alice. You've completed the class.\nExperience +2\n"
        self.assertEqual(expected, _.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_action_valid_incorrect_answer_in_boss_room(self, _):
        test_map = generate_map()
        test_character = {
            "user_name": "Alice",
            "location": (4, 4),
            "in_question": True,
            "health": 10,
            "experience": 2,
            "level": 1
        }
        question = (
            "What is the capital of France?", ({'A': 'London', 'B': 'Berlin', 'C': 'Madrid', 'D': 'Paris'}, 'd'))
        handle_user_action_for_question(test_map, test_character, question, "a")
        expected = "Incorrect! Alice, you loss extra health!\nHealth -3.\n"
        self.assertEqual(expected, _.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_action_valid_incorrect_answer_in_regular_room(self, _):
        test_map = generate_map()
        test_character = {
            "user_name": "Alice",
            "location": (2, 3),
            "in_question": True,
            "health": 10,
            "experience": 2,
            "level": 1
        }
        question = (
            "What is the capital of France?", ({'A': 'London', 'B': 'Berlin', 'C': 'Madrid', 'D': 'Paris'}, 'd'))
        handle_user_action_for_question(test_map, test_character, question, "a")
        expected = "Incorrect! Alice, you failed to complete the class.\nHealth -1.\n"
        self.assertEqual(expected, _.getvalue())
