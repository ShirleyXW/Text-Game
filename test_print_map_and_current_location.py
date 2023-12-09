import io

from unittest import TestCase
from unittest.mock import patch

from map import print_map_and_current_location, MAP_ROW_NUMBER, MAP_COLUMN_NUMBER, ROOM_TYPE_CLASSROOM, \
    ROOM_TYPE_ENTRANCE, ROOM_TYPE_BOSS_ROOM


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_correctly_prints_map_with_character_location_science_3(self, _):
        test_map = dict()
        for test_row in range(0, MAP_ROW_NUMBER):
            for test_column in range(0, MAP_COLUMN_NUMBER):
                test_map[(test_row, test_column)] = {'type': ROOM_TYPE_CLASSROOM,
                                                     'subject': ('Science', 'Sci'),
                                                     'subject_grade': 3,
                                                     'completed': False}
        test_character = {"location": (2, 2), "user_name": "Bob"}
        expected_output = ("┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 3  ┆┆ Sci 3  ┆┆ Sci 3  ┆┆ Sci 3  ┆┆ Sci 3  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 3  ┆┆ Sci 3  ┆┆ Sci 3  ┆┆ Sci 3  ┆┆ Sci 3  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐╔════════╗┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 3  ┆┆ Sci 3  ┆║ Sci 3  ║┆ Sci 3  ┆┆ Sci 3  ┆\n"
                           "┆        ┆┆        ┆║ (●v●)/ ║┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘╚════════╝└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 3  ┆┆ Sci 3  ┆┆ Sci 3  ┆┆ Sci 3  ┆┆ Sci 3  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Sci 3  ┆┆ Sci 3  ┆┆ Sci 3  ┆┆ Sci 3  ┆┆ Sci 3  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "You are now in Grade 3 Science class. You can start the class (enter 'x') or walk away.\n")

        print_map_and_current_location(test_map, test_character)
        self.assertEqual(expected_output, _.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_correctly_prints_map_with_character_location_highlighted_geography2(self, _):
        test_map = dict()
        for test_row in range(0, MAP_ROW_NUMBER):
            for test_column in range(0, MAP_COLUMN_NUMBER):
                test_map[(test_row, test_column)] = {'type': ROOM_TYPE_CLASSROOM,
                                                     'subject': ('Geography', 'Geo'),
                                                     'subject_grade': 2,
                                                     'completed': False}
        test_character = {"location": (0, 0), "user_name": "Bob"}
        expected_output = ("╔════════╗┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "║ Geo 2  ║┆ Geo 2  ┆┆ Geo 2  ┆┆ Geo 2  ┆┆ Geo 2  ┆\n"
                           "║ (●v●)/ ║┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "╚════════╝└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Geo 2  ┆┆ Geo 2  ┆┆ Geo 2  ┆┆ Geo 2  ┆┆ Geo 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Geo 2  ┆┆ Geo 2  ┆┆ Geo 2  ┆┆ Geo 2  ┆┆ Geo 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Geo 2  ┆┆ Geo 2  ┆┆ Geo 2  ┆┆ Geo 2  ┆┆ Geo 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ Geo 2  ┆┆ Geo 2  ┆┆ Geo 2  ┆┆ Geo 2  ┆┆ Geo 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "You are now in Grade 2 Geography class. "
                           "You can start the class (enter 'x') or walk away.\n")

        print_map_and_current_location(test_map, test_character)
        self.assertEqual(expected_output, _.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_correctly_prints_map_with_character_location_highlighted_CS_2(self, _):
        test_map = dict()
        for test_row in range(0, MAP_ROW_NUMBER):
            for test_column in range(0, MAP_COLUMN_NUMBER):
                test_map[(test_row, test_column)] = {'type': ROOM_TYPE_CLASSROOM,
                                                     'subject': ('Computer Science', 'C&S'),
                                                     'subject_grade': 2,
                                                     'completed': False}
        test_character = {"location": (0, 4), "user_name": "Bob"}
        expected_output = ("┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐╔════════╗\n"
                           "┆ C&S 2  ┆┆ C&S 2  ┆┆ C&S 2  ┆┆ C&S 2  ┆║ C&S 2  ║\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆║ (●v●)/ ║\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘╚════════╝\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ C&S 2  ┆┆ C&S 2  ┆┆ C&S 2  ┆┆ C&S 2  ┆┆ C&S 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ C&S 2  ┆┆ C&S 2  ┆┆ C&S 2  ┆┆ C&S 2  ┆┆ C&S 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ C&S 2  ┆┆ C&S 2  ┆┆ C&S 2  ┆┆ C&S 2  ┆┆ C&S 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "┆ C&S 2  ┆┆ C&S 2  ┆┆ C&S 2  ┆┆ C&S 2  ┆┆ C&S 2  ┆\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "You are now in Grade 2 Computer Science class. "
                           "You can start the class (enter 'x') or walk away.\n")

        print_map_and_current_location(test_map, test_character)
        self.assertEqual(expected_output, _.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_correctly_prints_map_with_character_location_highlighted_gate(self, _):
        test_map = dict()
        for test_row in range(0, MAP_ROW_NUMBER):
            for test_column in range(0, MAP_COLUMN_NUMBER):
                test_map[(test_row, test_column)] = {'type': ROOM_TYPE_CLASSROOM,
                                                     'subject': ('Science', 'Sci'),
                                                     'subject_grade': 2,
                                                     'completed': False}
        test_map[(0, 0)] = {
            "type": ROOM_TYPE_ENTRANCE
        }
        test_character = {"location": (0, 0), "user_name": "Bob"}
        expected_output = ("╔════════╗┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐\n"
                           "║ ░GATE░ ║┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆\n"
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
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘\n"
                           "Bob, you are standing in front of the school, try exploring!\n")

        print_map_and_current_location(test_map, test_character)
        self.assertEqual(expected_output, _.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_correctly_prints_map_with_character_location_highlighted_boss(self, _):
        test_map = dict()
        for test_row in range(0, MAP_ROW_NUMBER):
            for test_column in range(0, MAP_COLUMN_NUMBER):
                test_map[(test_row, test_column)] = {'type': ROOM_TYPE_CLASSROOM,
                                                     'subject': ('Science', 'Sci'),
                                                     'subject_grade': 2,
                                                     'completed': False}
        test_map[(4, 4)] = {
            "type": ROOM_TYPE_BOSS_ROOM
        }
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
                           "┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆║ ░BOSS░ ║\n"
                           "┆        ┆┆        ┆┆        ┆┆        ┆║ (●v●)/ ║\n"
                           "└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘╚════════╝\n"
                           "!!! ATTENTION !!! Bob, This is your final goal, fight for yourself!\n")

        print_map_and_current_location(test_map, test_character)
        self.assertEqual(expected_output, _.getvalue())
