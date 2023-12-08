import json
import os.path


USER_INFORMATION_FILE = "user_info.json"


def sync_user_info_to_file(character):
    """
    Synchronize user information to a file

    The function updates the user information file by replacing the existing information for the provided character.
    - If the user with the same user_name already exists, it removes the old information and adds the new character
    - If the user does not exist, it simply adds the character to the file

    :param character: dictionary containing information about the character
    :precondition: character dictionary must contain a valid key "user_name"
    :postcondition: update the user information file with the provided character
    :return: None

    >>> sync_user_info_to_file({"user_name": "Alice", "location": (0, 0)})
    >>> sync_user_info_to_file({"user_name": "Bob", "location": (2, 2)})
    """

    users = load_user_info_from_file()
    #
    for user_index in range(len(users)):
        if users[user_index]["user_name"] == character["user_name"]:
            users.remove(users[user_index])
            break
    users.append(character)

    dump_user_info_into_file(users)


def dump_user_info_into_file(users):
    """
    Dump user information into a file

    The function writes the provided user information into a file in JSON format

    :param users: a list of user information to be dumped into the file
    :precondition: users must be a list containing dictionaries with user information
    :postcondition: write the user information into the designated file in JSON format
    :return: None

    >>> dump_user_info_into_file([{"user_name": "Alice", "location": (0, 0)}, {"user_name": "Bob", "location": (2, 2)}])
    >>> dump_user_info_into_file([])
    """

    with open(USER_INFORMATION_FILE, "w") as file:
        json.dump(users, file)


def load_user_info_from_file():
    """
    Load user information from a file

    The function reads user information from a file in JSON format. If the file does not exist or is empty,
    an empty list is returned

    :precondition: None
    :postcondition: Reads user information from the designated file and returns a list of user information
    :return: List of user information.

    >>> dump_user_info_into_file([{"user_name": "Alice", "location": (0, 0)}, {"user_name": "Bob", "location": (2, 2)}])
    >>> load_user_info_from_file()
    [{'user_name': 'Alice', 'location': (0, 0)}, {'user_name': 'Bob', 'location': (2, 2)}]
    """

    if not os.path.isfile(USER_INFORMATION_FILE):
        return []

    # with open()
    with open(USER_INFORMATION_FILE, "r") as file_object:
        content = file_object.read()
        if len(content) == 0:
            return []
        else:
            users = json.loads(content)

    # Convert location from list to tuple
    for user in users:
        user["location"] = tuple(user["location"])
    return users

