
MAXIMUM_LEVEL = 3
EXPERIENCE_FOR_LEVEL_UP = 10

def make_board(rows, columns):
    game_map ={(row,column):'' for row in range(0,rows) for column in range(0,columns)}
    room_name=list()
    for _ in range(5):


def get_level_name(level):
    return {
        1: "Assistant Professors",
        2: "Lecturers",
        MAXIMUM_LEVEL: "Professors"
    }[level]

def make_character(player_name):
    return {
        "name": player_name,
        "level": 1,
        "health": 5,
        "wisdom": 0,
        "experience": 0,
    }


def character_has_leveled(character):
    return character["level"] < MAXIMUM_LEVEL and character["experience"] >= EXPERIENCE_FOR_LEVEL_UP


def execute_glow_up_protocol(character):
    character["experience"] = 0
    character["level"] += 1
    character["wisdom"] += 1


def game():
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_character("Player name")
    achieved_goal = False
    while not achieved_goal:
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character)
            describe_current_location(board, character)
            there_is_a_challenge = check_for_challenges()
            if there_is_a_challenge:
                execute_challenge_protocol(character)
            if character_has_leveled(character):
                execute_glow_up_protocol(character)
            achieved_goal = check_if_goal_attained(board, character)
        else:

def main():
    game()

if __name__ == "__manin__":
    main()
