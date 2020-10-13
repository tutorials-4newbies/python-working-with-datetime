import json

with open("users.json", "r") as users_file:
    users = json.loads(users_file.read())
    print(f'I have found {len(users)} users in the json file')

    user_1 = users[1]
    print(f'each user has those keys: {user_1.keys()}')
    print(f'user 1 was created at: {user_1["created"]}')
    print(f'user 1 was last_login was at: {user_1["last_login"]}')
    print(f'user_1["last_login"] type is:{type(user_1["last_login"])}')
    print('Good luck')