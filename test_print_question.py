from unittest import TestCase
from game import print_question
from unittest.mock import patch
import io


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_question(self, mock_stdout):
        question_instruction = \
            "Which of the following Arab countries does NOT have a flag containing only Pan-Arab colours?"
        formatted_question = (
            {
                "A": "Kuwait",
                "B": "United Arab Emirates",
                "C": "Jordan",
                "D": "Qatar"
            },
            "d"
        )

        print_question(question_instruction, formatted_question)
        expected = ("Which of the following Arab countries does NOT have a flag containing only Pan-Arab colours?\n"
                    " A : Kuwait\n"
                    " B : United Arab Emirates\n"
                    " C : Jordan\n"
                    " D : Qatar\n"
                    )
        self.assertEqual(expected, mock_stdout.getvalue())
