from unittest import TestCase

from map import generate_map, ROOM_TYPE_ENTRANCE, ROOM_TYPE_RELAX, ROOM_TYPE_CLASSROOM, ROOM_TYPE_BOSS_ROOM


class Test(TestCase):
    def test_generate_map_25_elements(self):
        expected_length = 25

        test_map = generate_map()
        actual_length = len(test_map)

        self.assertEqual(actual_length, expected_length)

    def test_generate_map_entrance_room(self):
        expected_type = ROOM_TYPE_ENTRANCE

        test_map = generate_map()
        actual_type = test_map[(0, 0)]["type"]

        self.assertEqual(actual_type, expected_type)

    def test_generate_map_relax_room(self):
        expected_type = ROOM_TYPE_RELAX

        test_map = generate_map()
        actual_type = test_map[(2, 2)]["type"]

        self.assertEqual(actual_type, expected_type)

    def test_generate_map_classroom(self):
        expected_type = ROOM_TYPE_CLASSROOM

        test_map = generate_map()
        actual_type = test_map[(1, 1)]["type"]

        self.assertEqual(actual_type, expected_type)

    def test_generate_map_boss_room(self):
        expected_type = ROOM_TYPE_BOSS_ROOM

        test_map = generate_map()
        actual_type = test_map[(4, 4)]["type"]

        self.assertEqual(actual_type, expected_type)
