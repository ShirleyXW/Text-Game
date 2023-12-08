from unittest import TestCase
from game import is_alive


class Test(TestCase):
    def test_is_alive_true(self):
        actual = is_alive({"health": 10, "user_name": "Bob"})
        expected = True
        self.assertEqual(expected, actual)

    def test_is_alive_false(self):
        actual = is_alive({"health": 0, "user_name": "Bob"})
        expected = False
        self.assertEqual(expected, actual)

