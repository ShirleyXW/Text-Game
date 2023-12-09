import sync_users_data


def input_user_name():
    """
    Prompt the user to input a valid username

    The function continuously prompts the user to enter a username until a valid one is provided
    A valid username contains only letters (e.g., Alice, alice, Bob, bob)

    :precondition: None
    :postcondition: prompt input
    :postcondition: get a valid username entered by the user
    :return: a string as username entered by the user.
    """
    while True:
        print("User name only accepts letters, eg: A,a,B,b\n")
        user_name = input("Enter your user name:\n")
        if user_name.isalpha():
            return user_name


def get_user_from_user_list(users_info, user_name):
    """
    Get user information from a list based on the username

    The function searches the list of user information for a user with the specified username
    If found, it returns the user's information; otherwise, it returns None

    :param users_info: a list containing dictionaries of user information
    :param user_name: a string
    :precondition: users_info must be a list of dictionaries with user information
    :precondition: user_name must be a string representing the username
    :postcondition: find the user information if the user is created
    :return: user information if True; otherwise, None.

    >>> users = [{"user_name": "Alice", "location": (0, 0)}, {"user_name": "Bob", "location": (2, 2)}]
    >>> get_user_from_user_list(users, "Alice")
    {'user_name': 'Alice', 'location': (0, 0)}
    >>> get_user_from_user_list(users, "Charlie")

    """
    for user in users_info:
        if user_name == user["user_name"]:
            return user
    return None


def create_new_character(user_name):
    """
    Create a new character with default attributes

    The function creates and returns a new character with the specified username and default attributes

    :param user_name: a string
    :precondition: user_name must be a string representing the username
    :postcondition: create a dictionary representing a new character with default attributes
    :return: a dictionary representing a new character with default attributes

    >>> create_new_character("Alice")
    {'user_name': 'Alice', 'location': (0, 0), 'in_question': False, 'level': 1, 'experience': 0, 'health': 5, 'max_health': 5, 'intelligence': 1}
    >>> create_new_character("Bob")
    {'user_name': 'Bob', 'location': (0, 0), 'in_question': False, 'level': 1, 'experience': 0, 'health': 5, 'max_health': 5, 'intelligence': 1}
    """
    return {
        "user_name": user_name,
        "location": (0, 0),
        "in_question": False,
        "level": 1,
        "experience": 0,
        "health": 5,
        "max_health": 5,
        "intelligence": 1
    }


def load_or_create_character():
    """
    Load an existing character or create a new one

    The function attempts to load an existing character based on the username
    If the character is not found, a new character is created and saved

    :precondition: None
    :postcondition: load an existing character if found; otherwise, creates and returns a new character
    :postcondition: set character's "in_question" status everytime when starting the game
    :return: an existing character if found; otherwise, a new character.
    """
    users_info = sync_users_data.load_user_info_from_file()

    user_name = input_user_name()

    character = get_user_from_user_list(users_info, user_name)
    if character is None:
        character = create_new_character(user_name)
        sync_users_data.sync_user_info_to_file(character)

    # Clear in class state when restarting
    character["in_question"] = False

    return character
