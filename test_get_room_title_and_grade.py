from unittest import TestCase
from map import get_room_title_and_grade, generate_map, ROOM_TYPE_CLASS_ROOM
from subjects import SUBJECTS


class Test(TestCase):
    def test_room_title_entrance(self):
        test_map = generate_map()
        row = 0
        column = 0
        expected = "\t🚪\t"
        actual = get_room_title_and_grade(test_map, row, column)
        self.assertEqual(expected, actual)

    def test_room_title_Boss(self):
        test_map = generate_map()
        row = 4
        column = 4
        expected = " !😈!\t"
        actual = get_room_title_and_grade(test_map, row, column)
        self.assertEqual(expected, actual)

    def test_room_title_Sci_2(self):
        test_map = {(2, 1): {"type": ROOM_TYPE_CLASS_ROOM, "subject": SUBJECTS[0], "subject_grade": 2}}
        row = 2
        column = 1
        expected = "Sci 2 "
        actual = get_room_title_and_grade(test_map, row, column)
        self.assertEqual(expected, actual)

    def test_room_title_Geo_2(self):
        test_map = {(3, 1): {"type": ROOM_TYPE_CLASS_ROOM, "subject": SUBJECTS[1], "subject_grade": 2}}
        row = 3
        column = 1
        expected = "Geo 2 "
        actual = get_room_title_and_grade(test_map, row, column)
        self.assertEqual(expected, actual)

    def test_room_title_Com_3(self):
        test_map = {(3, 2): {"type": ROOM_TYPE_CLASS_ROOM, "subject": SUBJECTS[2], "subject_grade": 3}}
        row = 3
        column = 2
        expected = "C&S 3 "
        actual = get_room_title_and_grade(test_map, row, column)
        self.assertEqual(expected, actual)
