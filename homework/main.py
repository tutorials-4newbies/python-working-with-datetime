import json

with open("users.json", "r") as users_file:
    users = json.loads(users_file.read())

    # --- Some demo code ----
    #
    # print(f'I have found {len(users)} users in the json file')
    # user_1 = users[1]
    # print(f'each user has those keys: {user_1.keys()}')
    # print(f'user 1 was created at: {user_1["created"]}')
    # print(f'user 1 was last_login was at: {user_1["last_login"]}')
    # print(f'user_1["last_login"] type is:{type(user_1["last_login"])}')

    # --- Code from here ----
    #
    # 1 -
    # באיזה חודש הכי הרבה משתמשים יצרו חשבון


    # 2 -
    # אילו משתמשים לא התחברו בשלושה חודשים האחרונים ולכן אפשר ל"סמן אותם" כלא פעילים


    # 3 -
    # למצוא 3 משתמשים שיצרו חשבון הכי מוקדם, והתחברו בחודש האחרון


