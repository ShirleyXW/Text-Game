from unittest import TestCase
from game import get_question
from unittest.mock import patch
import subjects


class Test(TestCase):
    @patch("random.randint", side_effect=[1])
    def test_get_science_question_1(self, _):
        gap_map = {
            (0, 2): {
                "subject": subjects.SCIENCE
            }
        }
        gamer = {
            "location": (0, 2)
        }

        question = {
            "question": "Which is the most abundant element in the universe?",
            "correct_answer": "Hydrogen",
            "incorrect_answers": [
                "Helium",
                "Lithium",
                "Oxygen"
            ]
        }
        actual = get_question(gap_map, gamer)
        self.assertEqual(question, actual)

    @patch("random.randint", side_effect=[1])
    def test_get_geograph_question_1(self, _):
        gap_map = {
            (1, 1): {
                "subject": subjects.GEOGRAPHY
            }
        }
        gamer = {
            "location": (1, 1)
        }

        question = {
            "question": "What is Laos?",
            "correct_answer": "Country",
            "incorrect_answers": [
                "Region",
                "River",
                "City"
            ]
        }
        actual = get_question(gap_map, gamer)
        self.assertEqual(question, actual)

    @patch("random.randint", side_effect=[1])
    def test_get_computer_question_1(self, _):
        gap_map = {
            (1, 3): {
                "subject": subjects.COMPUTER_SCIENCE
            }
        }
        gamer = {
            "location": (1, 3)
        }

        question = {
            "question": "When Gmail first launched, how much storage did it provide for your email?",
            "correct_answer": "1GB",
            "incorrect_answers": [
                "512MB",
                "5GB",
                "Unlimited"
            ]
        }
        actual = get_question(gap_map, gamer)
        self.assertEqual(question, actual)

    @patch("random.randint", side_effect=[1])
    def test_get_boss_question(self, _):
        gap_map = {
            (4, 4): {
            }
        }
        gamer = {
            "location": (4, 4)
        }

        question = {
            "question": "Hello!!! The last question is"
                        " \"Know your student~\"\n\nPlease find out who is the author creates this beautiful game?",
            "correct_answer": "Xinli Wang",
            "incorrect_answers": [
                "Shirley Wen",
                "Irene Wang",
                "Xinli Shirley"
            ]
        }
        actual = get_question(gap_map, gamer)
        self.assertEqual(question, actual)
