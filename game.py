import random

import user
import map
import subjects
import sync_users_data
import questions_bank


MAXIMUM_LEVEL = 3
EXPERIENCE_FOR_LEVEL_UP = 10

USER_INFORMATION_FILE = "user_info.json"


def get_question(game_map, character):
    if game_map[character["location"]]["subject"] == subjects.SCIENCE:
        question = questions_bank.NATURE_SCIENCE_QUESTIONS[random.randint(0,
                                                                          len(questions_bank.NATURE_SCIENCE_QUESTIONS) - 1)]
    elif game_map[character["location"]]["subject"] == subjects.GEOGRAPHY:
        question = questions_bank.GEOGRAPHY_QUESTIONS[random.randint(0, len(questions_bank.GEOGRAPHY_QUESTIONS) - 1)]
    elif game_map[character["location"]]["subject"] == subjects.COMPUTER_SCIENCE:
        question = questions_bank.COMPUTER_QUESTIONS[random.randint(0, len(questions_bank.COMPUTER_QUESTIONS) - 1)]
    else:
        question = questions_bank.BOSS_QUESTIONS[0]

    return question


def format_question(question):
    letters = [chr(letter) for letter in range(65, 69)]
    all_answers = [answer for answer in question["incorrect_answers"]]
    insert_index = random.randint(0, 3)
    correct_answer_letter = ''
    if insert_index == 0:
        correct_answer_letter = "a"
    elif insert_index == 1:
        correct_answer_letter = "b"
    elif insert_index == 2:
        correct_answer_letter = "c"
    elif insert_index == 3:
        correct_answer_letter = "d"
    all_answers.insert(insert_index, question["correct_answer"])
    multi_choice = dict(zip(letters, all_answers))

    return multi_choice, correct_answer_letter


def start_class(game_map, character):

    if game_map[character["location"]]["type"] != map.ROOM_TYPE_CLASS_ROOM:
        print("{}, you can't start class here".format(character["user_name"]))
        return

    elif game_map[character["location"]]["type"] == map.ROOM_TYPE_CLASS_ROOM:
        question = get_question(game_map, character)
        question_instruction = question["question"]
        formatted_question = format_question(question)
        character["in_question"] = True
        return question_instruction, formatted_question

    elif game_map[character["location"]]["type"] == map.ROOM_TYPE_BOSS_ROOM:
        question = get_question(game_map, character)
        question_instruction = question["question"]
        formatted_question = format_question(question)
        character["in_question"] = True
        return question_instruction, formatted_question


def is_alive():
    return True


def get_target_location(character, user_action):
    if user_action == "n":
        return character["location"][0] - 1, character["location"][1]
    elif user_action == "s":
        return character["location"][0] + 1, character["location"][1]
    elif user_action == "e":
        return character["location"][0], character["location"][1] + 1
    elif user_action == "w":
        return character["location"][0], character["location"][1] - 1
    else:
        raise Exception("Invalid action")


def move_character(game_map, character, user_action):
    target_location = get_target_location(character, user_action)
    character_level = character["level"]
    if target_location not in game_map:
        print("You can't go that way")
        return

    if target_location == map.BOSS_LOCATION and character_level < MAXIMUM_LEVEL:
        print("{} can't go there. Level up to 3, then give a try.".format(character["user_name"]))
        return

    character["location"] = target_location
    map.print_map_and_current_location(game_map,character)


def handle_user_action_for_question(game_map, character, current_question, user_action):

    if character["intelligence"] > game_map["subject_grade"]:
        auto_answer()
        if auto_answer():
            print("Correct answer, well done {} !".format(character["user_name"]))
            gain_experience(character)
            execute_glow_up_protocol(character)
            cross_out_the_room(game_map, character)

    else:
        loose_HP(character)
        print("Wrong answer {}. Keep going.".format(character["user_name"]))
    pass


def execute_glow_up_protocol(character):
    character["experience"] += 2


def game():
    character = user.load_or_create_character()
    game_map = map.generate_map()
    map.print_map_and_current_location(game_map, character)
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
            current_question = start_class(game_map, character)
            print(current_question[0], end="\n")
            for choice, answer in current_question[1][0].items():
                print(" {} : {}".format(choice, answer))

        elif user_action == 'i':
            # Print the character information
            pass

        elif user_action == 'm':
            # Print the map and current location
            map.print_map(game_map, character)

        elif user_action == 'q':
            # Exit the game
            print("Bye! {}".format(character["user_name"]))
            return
        else:
            print("Invalid option, {}.".format(character["user_name"]))

        sync_users_data.sync_user_info_to_file(character)


def main():
    game()


if __name__ == "__main__":
    main()
