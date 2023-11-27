
import user
import map
import subjects
import sync_users_data


MAXIMUM_LEVEL = 3
EXPERIENCE_FOR_LEVEL_UP = 10

USER_INFORMATION_FILE = "user_info.json"


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
    pass


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
            pass

        elif user_action == 'i':
            # Print the character information
            pass

        elif user_action == 'm':
            # Print the map and current location
            pass

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
