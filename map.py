import subjects

MAP_ROW_NUMBER = 5
MAP_COLUMN_NUMBER = 5

ROOM_TYPE_ENTRANCE = 1
ROOM_TYPE_CLASS_ROOM = 2
ROOM_TYPE_RELAX = 3
ROOM_TYPE_BOSS_ROOM = 4


def get_room_type(game_map, character):
    location = character["location"]
    if game_map[location]["type"] == ROOM_TYPE_CLASS_ROOM:
        return ("You are now in Grade {} {} class. You can start the class (enter 'x') or walk away."
                .format(game_map[location]["subject_grade"], game_map[location]["subject"][0]))
    elif game_map[location]["type"] == ROOM_TYPE_ENTRANCE:
        return "{}, you are standing in front of the school, try exploring!".format(character["user_name"])
    elif game_map[location]["type"] == ROOM_TYPE_RELAX:
        return ("Alright,{}, in the central garden 🍀, you find a book, reading and relaxing."
                .format(character["user_name"]))
    elif game_map[location]["type"] == ROOM_TYPE_BOSS_ROOM:
        return "!!! ATTENTION !!! {}, This is your final goal, fight for yourself!".format(character["user_name"])
    else:
        return ""


def get_room_title_and_grade(game_map, row, column):
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
    # Draw map and contain character inside
    print_map(game_map, character)
    # Print details of current location
    print(get_room_type(game_map, character))


def generate_map():
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
        "type": ROOM_TYPE_RELAX,
        "first_enter": True
    }
    game_map[(4, 4)] = {
        "type": ROOM_TYPE_BOSS_ROOM
    }
    return game_map

