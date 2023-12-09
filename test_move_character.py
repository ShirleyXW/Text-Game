from unittest import TestCase
from game import move_character
from unittest.mock import patch
import io
from map import generate_map


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_out_of_map(self, print_out):
        test_map = generate_map()
        test_character = {"user_name": "Alice", "location": (0, 0), "level": 2}
        move_character(test_map, test_character, "n")
        expected = "You can't go that way, Alice.\n"
        self.assertEqual(expected, print_out.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_can_not_access_before_level_3(self, print_out):
        test_map = generate_map()
        test_character = {"user_name": "Alice", "location": (4, 3), "level": 2}
        move_character(test_map, test_character, "e")
        expected = "Alice, you can't go there. Level up to 3, then give a try.\n"
        self.assertEqual(expected, print_out.getvalue())
