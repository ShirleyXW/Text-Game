import sync_users_data


def input_user_name():
    while True:
        print("User name only accepts letters, eg: A,a,B,b\n")
        user_name = input("Enter your user name:\n")
        if user_name.isalpha():
            return user_name


def get_user_from_user_list(users_info, user_name):
    for user in users_info:
        if user_name == user["user_name"]:
            return user
    return None


def create_new_character(user_name):
    return {
        "user_name": user_name,
        "location": (0, 0),
        "in_question": False,
        "level": 1,
        "experience": 0,
        "health": 5,
        "max_health": 5,
        "intelligence": 3
    }


def load_or_create_character():
    # TODO: handle exception for loading and matching error
    users_info = sync_users_data.load_user_info_from_file()

    user_name = input_user_name()

    character = get_user_from_user_list(users_info, user_name)
    if character is None:
        character = create_new_character(user_name)
        sync_users_data.sync_user_info_in_file(character)

    return character
