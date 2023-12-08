from unittest import TestCase
import io
import unittest.mock
from game import read_book_and_increase_intelligence


class Test(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_read_book_and_increase_intelligence_true(self, print_out):
        read_book_and_increase_intelligence(
            {"user_name": "Alice", "intelligence": 0, "location": (2, 2), "bonus_intelligence_gain": False})
        expected = ("\n  Education is not merely the imparting of knowledge, but the illumination of minds.\n"
                    "  It's a bridge, constructed with bricks of mutual enlightenment, where the essence is\n"
                    "  not just information but the ignition of curiosity and the cultivation of the power\n"
                    "  of wisdom. The true essence of teaching lies in guiding students to discover their\n"
                    "  own potential, enabling them to traverse unknown realms like explorers. Education is\n"
                    "  not just about imparting facts; it's about igniting the flame of learning within,\n"
                    "  allowing students to thrive and grow amidst the sparks of contemplation.\n\n"
                    "  The book says.\n\n  How do you like it, Alice?\nYour intelligence +3.\n")
        self.assertEqual(print_out.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_read_book_and_increase_intelligence_false(self, print_out):
        read_book_and_increase_intelligence(
            {"user_name": "Alice", "intelligence": 0, "location": (2, 2), "bonus_intelligence_gain": True})
        expected = "Seems the magic is gone. The book says. But reading is a not bad thing, Alice\n"
        self.assertEqual(expected, print_out.getvalue())
