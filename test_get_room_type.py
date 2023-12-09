from unittest import TestCase
from map import get_room_type, generate_map, ROOM_TYPE_CLASSROOM
from subjects import SUBJECTS


class Test(TestCase):
    def test_room_type_equals_entrance(self):
        test_map = generate_map()
        test_character = {"location": (0, 0), "user_name": "Alice"}
        expected = "Alice, you are standing in front of the school, try exploring!"
        actual = get_room_type(test_map, test_character)
        self.assertEqual(expected, actual)

    def test_room_type_equals_garden(self):
        test_map = generate_map()
        test_character = {"location": (2, 2), "user_name": "Alice"}
        expected = "Alright, Alice, in the central garden 🍀, you find a book, reading and relaxing."
        actual = get_room_type(test_map, test_character)
        self.assertEqual(expected, actual)

    def test_room_type_equals_science_2(self):
        test_character = {"location": (2, 1), "user_name": "Alice"}
        test_map = {(2, 1): {"type": ROOM_TYPE_CLASSROOM, "subject": SUBJECTS[0], "subject_grade": 2}}
        expected = "You are now in Grade 2 Science class. You can start the class (enter 'x') or walk away."
        actual = get_room_type(test_map, test_character)
        self.assertEqual(expected, actual)

    def test_room_type_equals_geograph_3(self):
        test_character = {"location": (3, 3), "user_name": "Alice"}
        test_map = {(3, 3): {"type": ROOM_TYPE_CLASSROOM, "subject": SUBJECTS[1], "subject_grade": 3}}
        expected = "You are now in Grade 3 Geography class. You can start the class (enter 'x') or walk away."
        actual = get_room_type(test_map, test_character)
        self.assertEqual(expected, actual)

    def test_room_type_equals_computer_1(self):
        test_character = {"location": (1, 3), "user_name": "Alice"}
        test_map = {(1, 3): {"type": ROOM_TYPE_CLASSROOM, "subject": SUBJECTS[2], "subject_grade": 1}}
        expected = "You are now in Grade 1 Computer Science class. You can start the class (enter 'x') or walk away."
        actual = get_room_type(test_map, test_character)
        self.assertEqual(expected, actual)

    def test_room_type_equals_boss_room(self):
        test_map = generate_map()
        test_character = {"location": (4, 4), "user_name": "Alice"}
        expected = "!!! ATTENTION !!! Alice, This is your final goal, fight for yourself!"
        actual = get_room_type(test_map, test_character)
        self.assertEqual(expected, actual)
