import random

import user
import map
import subjects
import sync_users_data
import questions_bank
import itertools

MAXIMUM_LEVEL = 3
EXPERIENCE_PER_CLASS = 2

EXPERIENCE_FOR_LEVEL_UP = 10

LEVEL_UP_INTELLIGENCE_GAIN = 3

USER_INFORMATION_FILE = "user_info.json"


def get_question(game_map, character):
    """

    :param game_map:
    :param character:
    :return:
    """
    if game_map[character["location"]].get("subject") == subjects.SCIENCE:
        question = questions_bank.NATURE_SCIENCE_QUESTIONS[
            random.randint(0, len(questions_bank.NATURE_SCIENCE_QUESTIONS) - 1)]
    elif game_map[character["location"]].get("subject") == subjects.GEOGRAPHY:
        question = questions_bank.GEOGRAPHY_QUESTIONS[random.randint(0, len(questions_bank.GEOGRAPHY_QUESTIONS) - 1)]
    elif game_map[character["location"]].get("subject") == subjects.COMPUTER_SCIENCE:
        question = questions_bank.COMPUTER_QUESTIONS[random.randint(0, len(questions_bank.COMPUTER_QUESTIONS) - 1)]
    else:
        question = questions_bank.BOSS_QUESTIONS[0]

    return question


def format_question(question):
    """

    :param question:
    :return:
    """
    letter = itertools.count(65)
    letters = []
    for element in range(65, 69):
        letters.append(chr(next(letter)))
    all_answers = [answer for answer in question["incorrect_answers"]]
    insert_index = random.randint(0, 3)
    correct_answer_letter = chr(97 + insert_index)
    all_answers.insert(insert_index, question["correct_answer"])
    multi_choice = dict(zip(letters, all_answers))
    return multi_choice, correct_answer_letter


def print_question(question_instruction, formatted_question):
    print(question_instruction)
    for choice, answer in formatted_question[0].items():
        print(" {} : {}".format(choice, answer))


def process_automatically(character, game_map):
    character["in_question"] = False
    print("This time your mastery of the subject captivated the class, "
          "and you effectively delivered this lesson! Keep trying {}".format(character["user_name"]))
    gain_experience(character)
    game_map[character["location"]]["completed"] = True


def start_class(game_map, character):
    character_location = character["location"]
    if game_map[character_location]["type"] == map.ROOM_TYPE_BOSS_ROOM:
        question = get_question(game_map, character)
        question_instruction = question["question"]
        formatted_question = format_question(question)
        character["in_question"] = True
        print_question(question_instruction, formatted_question)
        return question_instruction, formatted_question
    if game_map[character_location]["type"] != map.ROOM_TYPE_CLASS_ROOM:
        print("{}, you can't start class here".format(character["user_name"]))
        return
    if game_map[character_location]["completed"]:
        print("No class going on here.")
        return
    if is_class_proceeded_automatically(character, game_map[character_location]["subject_grade"]):
        process_automatically(character, game_map)
        return None
    else:
        print("Regrettably, your understanding of the subject falls short for teaching this class; "
              "you'll have to take an informed guess on following particular question.\n"
              "I believe you, {}. Give a try.".format(character["user_name"]))
        character["in_question"] = True
        question = get_question(game_map, character)
        question_instruction = question["question"]
        formatted_question = format_question(question)
        print_question(question_instruction, formatted_question)
        return question_instruction, formatted_question


def is_class_proceeded_automatically(character, subject_grade):
    # the higher "intelligence" is, the higher possibility succeed the class
    return random.randint(1, subject_grade * 5) <= character["intelligence"]


def is_alive(character):
    return character["health"] > 0


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


def read_book_and_increase_intelligence(character):
    if not character.get("bonus_intelligence_gain"):
        print("\n  Education is not merely the imparting of knowledge, but the illumination of minds. \n"
              "  It's a bridge, constructed with bricks of mutual enlightenment, where the essence is \n"
              "  not just information but the ignition of curiosity and the cultivation of the power \n"
              "  of wisdom. The true essence of teaching lies in guiding students to discover their \n"
              "  own potential, enabling them to traverse unknown realms like explorers. Education is \n"
              "  not just about imparting facts; it's about igniting the flame of learning within, \n"
              "  allowing students to thrive and grow amidst the sparks of contemplation.\n\n"
              "  The book says.\n")
        character["intelligence"] += LEVEL_UP_INTELLIGENCE_GAIN
        print("Your intelligence +{}.".format(LEVEL_UP_INTELLIGENCE_GAIN))
        character["bonus_intelligence_gain"] = True
    else:
        print("Seems the magic is gone. The book says.But reading is a not bad thing, {}".format(character["user_name"]))


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
    map.print_map_and_current_location(game_map, character)

    if game_map[target_location]["type"] == map.ROOM_TYPE_RELAX:
        read_book_and_increase_intelligence(character)


def handle_user_action_for_question(game_map, character, current_question, user_action):

    if user_action not in ("a", "b", "c", "d"):
        print("{}, invalid answer. Choose again.".format(character["user_name"]))
        question = get_question(game_map, character)
        question_instruction = question["question"]
        formatted_question = format_question(question)
        print_question(question_instruction, formatted_question)
        return

    if user_action == current_question[1][1]:
        if character["location"] == map.BOSS_LOCATION:
            print("Correct! You are now a SUPER teacher, {}!".format(character["user_name"]))
            exit()
        else:
            print("Correct! Good job, {}. You've completed the class.".format(character["user_name"]))
            gain_experience(character)
            game_map[character["location"]]["completed"] = True
    else:
        if character["location"] == map.BOSS_LOCATION:
            print("Incorrect! {}, you loss extra health!".format(character["user_name"]))
            loose_health(character, 3)
        else:
            print("Incorrect! {}, you failed to complete the class.".format(character["user_name"]))
            loose_health(character, 1)

    character["in_question"] = False


def loose_health(character, minus_health):
    print("Health -{}.".format(minus_health))
    character["health"] -= minus_health


def get_character_info(character):
    return ("\nCurrent character {} info:\n"
            "  Health        {}/{}\n"
            "  Level         {}\n"
            "  Intelligence  {}\n"
            "  Experience    {}/{}\n"
            ).format(character["user_name"], character["health"], character["max_health"],
                     character["level"],
                     character["intelligence"],
                     character["experience"], EXPERIENCE_FOR_LEVEL_UP)


def check_level_up(character):
    if character["level"] >= MAXIMUM_LEVEL or character["experience"] < EXPERIENCE_FOR_LEVEL_UP:
        return False

    character["level"] += character["experience"] // EXPERIENCE_FOR_LEVEL_UP
    character["experience"] = character["experience"] % EXPERIENCE_FOR_LEVEL_UP
    character["intelligence"] += LEVEL_UP_INTELLIGENCE_GAIN

    print("You leveled up! Your intelligence +{}.".format(LEVEL_UP_INTELLIGENCE_GAIN))
    print(get_character_info(character))


def gain_experience(character):
    character["experience"] += EXPERIENCE_PER_CLASS
    print("Experience +{}".format(EXPERIENCE_PER_CLASS))
    check_level_up(character)


def game():
    character = user.load_or_create_character()
    game_map = map.generate_map()
    map.print_map_and_current_location(game_map, character)
    current_question = None

    # Exit game in handle_user_action() when
    # 1. health is zero 2. user types 'q' 3. Boss room is completed
    while True:
        if not is_alive(character):
            print("Sorry {}, your journey is over. Try next time.".format(character["user_name"]))
            sync_users_data.sync_user_info_to_file(character)
            return

        user_action = input().lower()
        if user_action == "":
            continue

        # If character's status is in the class ,then check answer
        if character["in_question"] is True:
            handle_user_action_for_question(game_map, character, current_question, user_action)
            sync_users_data.sync_user_info_to_file(character)
            continue

        if user_action in ['n', 's', 'w', 'e']:
            move_character(game_map, character, user_action)
        elif user_action == 'x':
            # Start the game
            current_question = start_class(game_map, character)
        elif user_action == 'i':
            # Print the character information
            print(get_character_info(character))

        elif user_action == 'm':
            # Print the map and current location
            map.print_map(game_map, character)

        elif user_action == 'q':
            # Exit the game
            print("Bye! {}".format(character["user_name"]))
            sync_users_data.sync_user_info_to_file(character)
            return
        else:
            print("Invalid option, {}.".format(character["user_name"]))

        sync_users_data.sync_user_info_to_file(character)


def main():
    game()


if __name__ == "__main__":
    main()
