from unittest import TestCase
from game import format_question
from unittest.mock import patch


class Test(TestCase):
    @patch("random.randint", side_effect=[0])
    def test_formatted_question_with_correct_answer_a(self, _):
        expected = (
            {
                "A": "Qatar",
                "B": "Kuwait",
                "C": "United Arab Emirates",
                "D": "Jordan"
            },
            "a"
        )
        question = {
            "question": "Which of the following Arab countries does NOT have a flag containing only Pan-Arab colours?",
            "correct_answer": "Qatar",
            "incorrect_answers": [
                "Kuwait",
                "United Arab Emirates",
                "Jordan"
            ]
        }
        actual = format_question(question)
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[1])
    def test_formatted_question_with_correct_answer_b(self, _):
        expected = (
            {
                "A": "Kuwait",
                "B": "Qatar",
                "C": "United Arab Emirates",
                "D": "Jordan"
            },
            "b"
        )
        question = {
            "question": "Which of the following Arab countries does NOT have a flag containing only"
                        " Pan-Arab colours?",
            "correct_answer": "Qatar",
            "incorrect_answers": [
                "Kuwait",
                "United Arab Emirates",
                "Jordan"
            ]
        }
        actual = format_question(question)
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[2])
    def test_formatted_question_with_correct_answer_c(self, _):
        expected = (
            {
                "A": "Kuwait",
                "B": "United Arab Emirates",
                "C": "Qatar",
                "D": "Jordan"
            },
            "c"
        )
        question = {
            "question": "Which of the following Arab countries does NOT have a flag containing only Pan-Arab colours?",
            "correct_answer": "Qatar",
            "incorrect_answers": [
                "Kuwait",
                "United Arab Emirates",
                "Jordan"
            ]
        }
        actual = format_question(question)
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[3])
    def test_formatted_question_with_correct_answer_d(self, _):
        expected = (
            {
                "A": "Kuwait",
                "B": "United Arab Emirates",
                "C": "Jordan",
                "D": "Qatar"
            },
            "d"
        )
        question = {
            "question": "Which of the following Arab countries does NOT have a flag containing only Pan-Arab colours?",
            "correct_answer": "Qatar",
            "incorrect_answers": [
                "Kuwait",
                "United Arab Emirates",
                "Jordan"
            ]
        }
        actual = format_question(question)
        self.assertEqual(expected, actual)
