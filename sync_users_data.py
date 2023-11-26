import json

USER_INFORMATION_FILE = "user_info.json"


def sync_user_info_in_file(character):
    users = load_user_info_from_file()
    #
    for user_index in range(len(users)):
        if users[user_index]["user_name"] == character["user_name"]:
            users.remove(users[user_index])
            break
    users.append(character)

    dump_user_info_into_file(users)


def dump_user_info_into_file(users):
    with open(USER_INFORMATION_FILE, "w") as file:
        json.dump(users, file)


def load_user_info_from_file():
    # with open()
    with open(USER_INFORMATION_FILE) as file_object:
        users = json.load(file_object)

    # Convert location from list to tuple
    for user in users:
        user["location"] = tuple(user["location"])
    return users


# Test
if __name__ == "__main__":
    dump_user_info_into_file([
        {
            "user_name": "Hugo",
            "location": (1, 2),
            "in_class": False,
            "level": 3,
            "experience": 0,
            "health": 5,
            "intelligence": 3
        },
        {
            "user_name": "Hugo_stupid",
            "location": (2, 2),
            "in_class": False,
            "level": 3,
            "experience": 0,
            "health": 5,
            "intelligence": 3
        }

    ])

    print(load_user_info_from_file())

    sync_user_info_in_file(
        {
            "user_name": "Hugo",
            "location": (3, 3),
            "in_class": True,
            "level": 6,
            "experience": 0,
            "health": 5
        }
    )
    print(load_user_info_from_file())

    sync_user_info_in_file({
        "user_name": "Hugo_2",
        "location": (4, 4),
        "in_class": False,
        "level": 16,
        "experience": 0,
        "health": 5
    })
    print(load_user_info_from_file())
