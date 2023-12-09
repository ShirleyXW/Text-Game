import io
from unittest import TestCase
from unittest.mock import patch
from map import print_map, MAP_ROW_NUMBER, MAP_COLUMN_NUMBER, ROOM_TYPE_CLASSROOM


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_correctly_prints_map_with_character_location_highlighted(self, _):
        test_map = dict()
        for test_row in range(0, MAP_ROW_NUMBER):
            for test_column in range(0, MAP_COLUMN_NUMBER):
                test_map[(test_row, test_column)] = {'type': ROOM_TYPE_CLASSROOM,
                                                     'subject': ('Science', 'Sci'),
                                                     'subject_grade': 2,
                                                     'completed': False}
        test_character = {"location": (2, 2), "user_name": "Bob"}
        expected_output = ("┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐╔════════╗┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆║ Sci 2  ║┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "┆        ┆┆        ┆║ (●v●)/ ║┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘╚════════╝└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n")

        print_map(test_map, test_character)
        self.assertEqual(expected_output, _.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_correctly_prints_map_with_character_location_highlighted_north_west(self, _):
        test_map = dict()
        for test_row in range(0, MAP_ROW_NUMBER):
            for test_column in range(0, MAP_COLUMN_NUMBER):
                test_map[(test_row, test_column)] = {'type': ROOM_TYPE_CLASSROOM,
                                                     'subject': ('Science', 'Sci'),
                                                     'subject_grade': 2,
                                                     'completed': False}
        test_character = {"location": (0, 0), "user_name": "Bob"}
        expected_output = ("╔════════╗┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "║ Sci 2  ║┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "║ (●v●)/ ║┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "╚════════╝└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n")

        print_map(test_map, test_character)
        self.assertEqual(expected_output, _.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_correctly_prints_map_with_character_location_highlighted_north_east(self, _):
        test_map = dict()
        for test_row in range(0, MAP_ROW_NUMBER):
            for test_column in range(0, MAP_COLUMN_NUMBER):
                test_map[(test_row, test_column)] = {'type': ROOM_TYPE_CLASSROOM,
                                                     'subject': ('Science', 'Sci'),
                                                     'subject_grade': 2,
                                                     'completed': False}
        test_character = {"location": (0, 4), "user_name": "Bob"}
        expected_output = ("┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐╔════════╗\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆║ Sci 2  ║\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆║ (●v●)/ ║\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘╚════════╝\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n")

        print_map(test_map, test_character)
        self.assertEqual(expected_output, _.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_correctly_prints_map_with_character_location_highlighted_south_west(self, _):
        test_map = dict()
        for test_row in range(0, MAP_ROW_NUMBER):
            for test_column in range(0, MAP_COLUMN_NUMBER):
                test_map[(test_row, test_column)] = {'type': ROOM_TYPE_CLASSROOM,
                                                     'subject': ('Science', 'Sci'),
                                                     'subject_grade': 2,
                                                     'completed': False}
        test_character = {"location": (4, 0), "user_name": "Bob"}
        expected_output = ("┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "╔════════╗┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "║ Sci 2  ║┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "║ (●v●)/ ║┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "╚════════╝└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n")

        print_map(test_map, test_character)
        self.assertEqual(expected_output, _.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_correctly_prints_map_with_character_location_highlighted_south_east(self, _):
        test_map = dict()
        for test_row in range(0, MAP_ROW_NUMBER):
            for test_column in range(0, MAP_COLUMN_NUMBER):
                test_map[(test_row, test_column)] = {'type': ROOM_TYPE_CLASSROOM,
                                                     'subject': ('Science', 'Sci'),
                                                     'subject_grade': 2,
                                                     'completed': False}
        test_character = {"location": (4, 4), "user_name": "Bob"}
        expected_output = ("┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐╔════════╗\n"
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆║ Sci 2  ║\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆║ (●v●)/ ║\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘╚════════╝\n")

        print_map(test_map, test_character)
        self.assertEqual(expected_output, _.getvalue())
