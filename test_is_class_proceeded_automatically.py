from unittest import TestCase
from unittest.mock import patch
from game import is_class_proceeded_automatically


class Test(TestCase):
    @patch("random.randint", side_effect=[1])
    def test_is_class_proceeded_automatically(self, _):
        expected = True
        actual = is_class_proceeded_automatically({"intelligence": 2, "user_name": "Alice"}, 2)
        self.assertEqual(expected, actual)
