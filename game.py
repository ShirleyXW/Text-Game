
MAP_ROW_NUMBER = 5
MAP_COLUMN_NUMBER = 5

MAXIMUM_LEVEL = 3
EXPERIENCE_FOR_LEVEL_UP = 10

def generate_map():
    game_map ={(row,column):'' for row in range(0,MAP_ROW_NUMBER) for column in range(0,MAP_COLUMN_NUMBER)}
    room_name=list()
    for _ in range(5):
        pass
    return game_map


def get_level_name(level):
    return {
        1: "Assistant Professors",
        2: "Lecturers",
        MAXIMUM_LEVEL: "Professors"
    }[level]

def write_user_info_into_disk():


def load_or_create_character():

    users = load_user_from_file()

    user_credential = get_user_credential()
    if user_exists():
        # TODO: return corespoinding user info
    else:
        # TODO: create new user
        create_new_character()
        # TODO: write into disk



def character_has_leveled(character):
    return character["level"] < MAXIMUM_LEVEL and character["experience"] >= EXPERIENCE_FOR_LEVEL_UP


def execute_glow_up_protocol(character):
    character["experience"] = 0
    character["level"] += 1
    character["wisdom"] += 1


def game():
    character=load_or_create_character()
    game_map = generate_map()
    print_map_and_current_location(game_map, character)

    # Exit game in handle_user_action() when
    # 1. HP is zero 2. user types 'q' 3. Boss room is completed
    while True:
        handle_user_action(game_map, character, input())












    # while not achieved_goal:
    #     describe_current_location(board, character)
    #     direction = get_user_choice()
    #     valid_move = validate_move(board, character, direction)
    #     if valid_move:
    #         move_character(character)
    #         describe_current_location(board, character)
    #         there_is_a_challenge = check_for_challenges()
    #         if there_is_a_challenge:
    #             execute_challenge_protocol(character)
    #         if character_has_leveled(character):
    #             execute_glow_up_protocol(character)
    #         achieved_goal = check_if_goal_attained(board, character)
    #     else:

def main():
    game()

if __name__ == "__manin__":
    main()
