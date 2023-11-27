import random

import user


MAP_ROW_NUMBER = 5
MAP_COLUMN_NUMBER = 5

ROOM_TYPE_ENTRANCE = 1
ROOM_TYPE_CLASS_ROOM = 2
ROOM_TYPE_RELAX = 3
ROOM_TYPE_BOSS_ROOM = 4

SCIENCE = ("Science", "Sci")
GEOGRAPHY = ("Geography", "Geo")
COMPUTER_SCIENCE = ("Computer Science", "C&S")
SUBJECTS = (SCIENCE, GEOGRAPHY, COMPUTER_SCIENCE)

MAXIMUM_LEVEL = 3
EXPERIENCE_FOR_LEVEL_UP = 10

USER_INFORMATION_FILE = "user_info.json"


def get_room_title_and_grade(game_map, row, column):
    if game_map[(row, column)]["type"] == ROOM_TYPE_CLASS_ROOM:
        room_title = " {}{} ".format(game_map[(row, column)]["subject"][1], game_map[(row, column)]["subject_grade"])
        return room_title
    elif game_map[(row, column)]["type"] == ROOM_TYPE_ENTRANCE:
        return  "\t🚪\t"
    elif game_map[(row, column)]["type"] == ROOM_TYPE_RELAX:
        return "\t🍀\t"
    elif game_map[(row, column)]["type"] == ROOM_TYPE_BOSS_ROOM:
        return " !😈!\t"
    else:
        return ""



def print_map(game_map,character):
    for row in range(MAP_ROW_NUMBER):
        line_1 =""
        line_2 =""
        line_3 =""
        line_4 =""
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
    print_map(game_map,character)
    # Print details of current location
    print("Welcome to {}, {}".format(game_map["type"],character["user_name"]))



def subjects():
    subject = SUBJECTS[random.randint(0,2)]
    return subject


def subject_grades(row, column):
    if row <=2 and column <=2 :
        return 2
    elif row <= 3 and column <= 3 :
        return 3
    else:
        return 4


def generate_map():
    game_map ={
        (row,column):{
            "type": ROOM_TYPE_CLASS_ROOM,
            "subject": subjects(),
            "subject_grade": subject_grades(row,column),
            "completed": False
        }
        for row in range(0,MAP_ROW_NUMBER) for column in range(0,MAP_COLUMN_NUMBER)
    }
    game_map[(0,0)] = {
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



def get_level_name(level):
    return {
        1: "Assistant Professors",
        2: "Lecturers",
        MAXIMUM_LEVEL: "Professors"
    }[level]


def character_has_leveled(character):
    return character["level"] < MAXIMUM_LEVEL and character["experience"] >= EXPERIENCE_FOR_LEVEL_UP


def execute_glow_up_protocol(character):
    character["experience"] = 0
    character["level"] += 1
    character["wisdom"] += 1


def game():
    character= user.load_or_create_character()
    game_map = generate_map()
    print_map_and_current_location(game_map, character)
    current_question = None

    # Exit game in handle_user_action() when
    # 1. HP is zero 2. user types 'q' 3. Boss room is completed
    while True:
        if not is_alive():
            print("Sorry {}, your journey is over. Try next time.".format(character["user_name"]))
            return

        user_action = input().lower()
        if user_action == "":
            continue

        # If character's status is in the class ,then check answer
        if character["in_question"] is True:
            handle_user_action_for_question(game_map, character, current_question, user_action)

        if user_action in ['n', 's', 'w', 'e']:
            move_character(game_map, character, user_action)
        elif user_action == 'x':
            # Start the game

        elif user_action == 'i':
            # Print the character information

        elif user_action == 'm':
            #Print the map and current location

        elif user_action == 'q':
            # Exit the game
            print("Bye! {}".format(character["user_name"]))
            return
        else:
            print("Invalid option, {}.".format(character["user_name"]))



def main():
    game()

if __name__ == "__manin__":
    main()
