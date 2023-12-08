import subjects

MAP_ROW_NUMBER = 5
MAP_COLUMN_NUMBER = 5

ROOM_TYPE_ENTRANCE = 1
ROOM_TYPE_CLASS_ROOM = 2
ROOM_TYPE_RELAX = 3
ROOM_TYPE_BOSS_ROOM = 4

BOSS_LOCATION = (MAP_ROW_NUMBER - 1, MAP_COLUMN_NUMBER - 1)


def get_room_type(game_map, character):
    """
    Get the room type of the current location

    :param game_map: The map of the school
    :param character: The character's information
    :precondition: `game_map` must be a dictionary representing the map of the school
                   `character` must be a dictionary containing information about the character
    :postcondition: Returns a string describing the room type based on the character's current location
    :return: A string describing the room type

    Examples:
        >>> test_map = generate_map()
        >>> test_character = {"location": (0, 0), "user_name": "Alice"}
        >>> get_room_type(test_map, test_character)
        'Alice, you are standing in front of the school, try exploring!'

        >>> test_map = generate_map()
        >>> test_character = {"location": (2, 2), "user_name": "Bob"}
        >>> get_room_type(test_map, test_character)
        'Alright, Bob, in the central garden 🍀, you find a book, reading and relaxing.'
    """
    location = character["location"]
    if game_map[location]["type"] == ROOM_TYPE_CLASS_ROOM:
        return ("You are now in Grade {} {} class. You can start the class (enter 'x') or walk away."
                .format(game_map[location]["subject_grade"], game_map[location]["subject"][0]))
    elif game_map[location]["type"] == ROOM_TYPE_ENTRANCE:
        return "{}, you are standing in front of the school, try exploring!".format(character["user_name"])
    elif game_map[location]["type"] == ROOM_TYPE_RELAX:
        return ("Alright, {}, in the central garden 🍀, you find a book, reading and relaxing."
                .format(character["user_name"]))
    elif game_map[location]["type"] == ROOM_TYPE_BOSS_ROOM:
        return "!!! ATTENTION !!! {}, This is your final goal, fight for yourself!".format(character["user_name"])
    else:
        return ""


def get_room_title_and_grade(game_map, row, column):
    """
    Get the room title and grade for a given row and column

    :param game_map: a dictionary consisting of the information of the school
    :param row: a positive integer
    :param column: a positive integer
    :precondition: game_map must be a dictionary representing the map of the school
    :precondition: row must be a positive integer representing valid indices in the map
    :precondition: column must be a positive integer representing valid indices in the map
    :postcondition: Returns a string representing the room title and grade based on the provided row and column
    :return: The room title as a string

   >>> test_map = dict()
    >>> for test_row in range(0, MAP_ROW_NUMBER):
    ...     for test_column in range(0, MAP_COLUMN_NUMBER):
    ...         test_map[(test_row, test_column)] = {'type': ROOM_TYPE_CLASS_ROOM,
    ...              'subject': ('Science', 'Sci'),
    ...              'subject_grade': 2,
    ...              'completed': False}
    >>> get_room_title_and_grade(test_map, 1, 1)
    'Sci 2 '
    >>> test_map = dict()
    >>> for test_row in range(0, MAP_ROW_NUMBER):
    ...     for test_column in range(0, MAP_COLUMN_NUMBER):
    ...         test_map[(test_row, test_column)] = {'type': ROOM_TYPE_CLASS_ROOM,
    ...              'subject': ('Geography', 'Geo'),
    ...              'subject_grade': 3,
    ...              'completed': False}
    >>> get_room_title_and_grade(test_map, 2, 3)
    'Geo 3 '
    """
    if game_map[(row, column)]["type"] == ROOM_TYPE_CLASS_ROOM:
        room_title = "{} {} ".format(game_map[(row, column)]["subject"][1], game_map[(row, column)]["subject_grade"])
        return room_title
    elif game_map[(row, column)]["type"] == ROOM_TYPE_ENTRANCE:
        return "\t🚪\t"
    elif game_map[(row, column)]["type"] == ROOM_TYPE_RELAX:
        return "\t🍀\t"
    elif game_map[(row, column)]["type"] == ROOM_TYPE_BOSS_ROOM:
        return " !😈!\t"
    else:
        return ""


def print_map(game_map, character):
    """
    Print the map with the character's current location

    :param game_map: a dictionary consisting of the information of the school
    :param character: a dictionary consisting of character's information
    :precondition: game_map must be a dictionary representing the map of the school
    :precondition: character must be a dictionary containing information about the character
    :postcondition: draw the map with the character's current location highlighted
    :return: None

    >>> test_map = dict()
    >>> for test_row in range(0, MAP_ROW_NUMBER):
    ...     for test_column in range(0, MAP_COLUMN_NUMBER):
    ...         test_map[(test_row, test_column)] = {'type': ROOM_TYPE_CLASS_ROOM,
    ...              'subject': ('Science', 'Sci'),
    ...              'subject_grade': 2,
    ...              'completed': False}
    >>> test_character = {"location": (2, 2), "user_name": "Bob"}
    >>> print_map(test_map, test_character)
    ┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐
    ┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆
    ┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆
    └╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘
    ┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐
    ┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆
    ┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆
    └╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘
    ┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐╔════════╗┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐
    ┆ Sci 2  ┆┆ Sci 2  ┆║ Sci 2  ║┆ Sci 2  ┆┆ Sci 2  ┆
    ┆        ┆┆        ┆║ ⎝(◕_◕)⎠║┆        ┆┆        ┆
    └╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘╚════════╝└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘
    ┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐
    ┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆
    ┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆
    └╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘
    ┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐
    ┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆
    ┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆
    └╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘
   >>> test_map = dict()
    >>> for test_row in range(0, MAP_ROW_NUMBER):
    ...     for test_column in range(0, MAP_COLUMN_NUMBER):
    ...         test_map[(test_row, test_column)] = {'type': ROOM_TYPE_CLASS_ROOM,
    ...              'subject': ('Geography', 'Geo'),
    ...              'subject_grade': 3,
    ...              'completed': False}
    >>> test_character = {"location": (3, 4), "user_name": "Bob"}
    >>> print_map(test_map, test_character)
    ┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐
    ┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆
    ┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆
    └╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘
    ┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐
    ┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆
    ┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆
    └╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘
    ┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐
    ┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆
    ┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆
    └╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘
    ┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐╔════════╗
    ┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆║ Geo 3  ║
    ┆        ┆┆        ┆┆        ┆┆        ┆║ ⎝(◕_◕)⎠║
    └╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘╚════════╝
    ┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐
    ┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆
    ┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆
    └╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘

    """
    for row in range(MAP_ROW_NUMBER):
        line_1 = ""
        line_2 = ""
        line_3 = ""
        line_4 = ""
        for column in range(MAP_COLUMN_NUMBER):
            if character["location"] == (row, column):
                line_1 += "╔════════╗"
                line_2 += "║ {} ║".format(get_room_title_and_grade(game_map, row, column))
                line_3 += "║ {}║".format("⎝(◕_◕)⎠")
                line_4 += "╚════════╝"
            else:
                line_1 += "┌╌╌╌╌╌╌╌╌┐"
                line_2 += "┆ {} ┆".format(get_room_title_and_grade(game_map, row, column))
                line_3 += "┆        ┆"
                line_4 += "└╌╌╌╌╌╌╌╌┘"
        print(line_1)
        print(line_2)
        print(line_3)
        print(line_4)


def print_map_and_current_location(game_map, character):
    """
    Print the map and the details of the character's current location.

    :param game_map: a dictionary consisting of the information of the school
    :param character: a dictionary consisting of character's information
    :precondition: game_map must be a dictionary representing the map of the school
    :precondition: character must be a dictionary containing information about the character
    :postcondition: print the map with the character's current location highlighted
                    and details of the current location are printed.
    :return: None

     >>> test_map = dict()
    >>> for test_row in range(0, MAP_ROW_NUMBER):
    ...     for test_column in range(0, MAP_COLUMN_NUMBER):
    ...         test_map[(test_row, test_column)] = {'type': ROOM_TYPE_CLASS_ROOM,
    ...              'subject': ('Science', 'Sci'),
    ...              'subject_grade': 2,
    ...              'completed': False}
    >>> test_character = {"location": (2, 2), "user_name": "Bob"}
    >>> print_map_and_current_location(test_map, test_character)
    ┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐
    ┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆
    ┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆
    └╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘
    ┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐
    ┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆
    ┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆
    └╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘
    ┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐╔════════╗┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐
    ┆ Sci 2  ┆┆ Sci 2  ┆║ Sci 2  ║┆ Sci 2  ┆┆ Sci 2  ┆
    ┆        ┆┆        ┆║ ⎝(◕_◕)⎠║┆        ┆┆        ┆
    └╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘╚════════╝└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘
    ┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐
    ┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆
    ┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆
    └╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘
    ┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐
    ┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆┆ Sci 2  ┆
    ┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆
    └╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘
    You are now in Grade 2 Science class. You can start the class (enter 'x') or walk away.
   >>> test_map = dict()
    >>> for test_row in range(0, MAP_ROW_NUMBER):
    ...     for test_column in range(0, MAP_COLUMN_NUMBER):
    ...         test_map[(test_row, test_column)] = {'type': ROOM_TYPE_CLASS_ROOM,
    ...              'subject': ('Geography', 'Geo'),
    ...              'subject_grade': 3,
    ...              'completed': False}
    >>> test_character = {"location": (1, 2), "user_name": "Bob"}
    >>> print_map_and_current_location(test_map, test_character)
    ┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐
    ┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆
    ┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆
    └╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘
    ┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐╔════════╗┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐
    ┆ Geo 3  ┆┆ Geo 3  ┆║ Geo 3  ║┆ Geo 3  ┆┆ Geo 3  ┆
    ┆        ┆┆        ┆║ ⎝(◕_◕)⎠║┆        ┆┆        ┆
    └╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘╚════════╝└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘
    ┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐
    ┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆
    ┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆
    └╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘
    ┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐
    ┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆
    ┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆
    └╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘
    ┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐┌╌╌╌╌╌╌╌╌┐
    ┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆┆ Geo 3  ┆
    ┆        ┆┆        ┆┆        ┆┆        ┆┆        ┆
    └╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘└╌╌╌╌╌╌╌╌┘
    You are now in Grade 3 Geography class. You can start the class (enter 'x') or walk away.
    """
    # Draw map and contain character inside
    print_map(game_map, character)
    # Print details of current location
    print(get_room_type(game_map, character))


def generate_map():
    """
    Generate the initial map of the school

    :precondition: None
    :postcondition: generate a dictionary representing the initial map of the school
    :return: a map as a dictionary

    >>> test_map = generate_map()
    >>> test_map[(0, 0)]["type"]
    1
    >>> test_map = generate_map()
    >>> test_map[(2, 2)]["type"]
    3
    """
    game_map = {
        (row, column): {
            "type": ROOM_TYPE_CLASS_ROOM,
            "subject": subjects.subjects(),
            "subject_grade": subjects.subject_grades(row, column),
            "completed": False
        }
        for row in range(0, MAP_ROW_NUMBER) for column in range(0, MAP_COLUMN_NUMBER)
    }
    game_map[(0, 0)] = {
        "type": ROOM_TYPE_ENTRANCE
    }
    game_map[(2, 2)] = {
        "type": ROOM_TYPE_RELAX
    }
    game_map[(4, 4)] = {
        "type": ROOM_TYPE_BOSS_ROOM
    }
    return game_map
