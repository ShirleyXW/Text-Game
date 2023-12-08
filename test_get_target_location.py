from unittest import TestCase
from game import get_target_location


class Test(TestCase):
    def test_get_target_location_go_north(self):
        actual = get_target_location({"user_name": "Alice", "location": (2, 2)}, "n")
        expected = (1, 2)
        self.assertEqual(expected, actual)

    def test_get_target_location_go_south(self):
        actual = get_target_location({"user_name": "Alice", "location": (2, 2)}, "s")
        expected = (3, 2)
        self.assertEqual(expected, actual)

    def test_get_target_location_go_west(self):
        actual = get_target_location({"user_name": "Alice", "location": (2, 2)}, "w")
        expected = (2, 1)
        self.assertEqual(expected, actual)

    def test_get_target_location_go_east(self):
        actual = get_target_location({"user_name": "Alice", "location": (2, 2)}, "e")
        expected = (2, 3)
        self.assertEqual(expected, actual)

    def test_get_target_location_go_out_of_board(self):
        with self.assertRaises(Exception):
            test_character = {"user_name": "Alice", "location": (0, 0)}
            get_target_location(test_character, "r")
