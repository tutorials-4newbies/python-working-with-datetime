import json
from datetime import date, datetime, time, timedelta

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
    # באיזה שעה משתמש עם ID=42 יצר חשבון
    user_42 = None
    for user in users:
        if user['id'] == 42:
            user_42 = user

    user_42_created_datetime = datetime.strptime(user_42['created'], "%Y-%m-%dT%H:%M:%SZ")
    user_42_created_at_time_string = datetime.strftime(user_42_created_datetime, "%H:%M")
    print(f'user with id 42 was created at {user_42_created_at_time_string}')

    # 2 -
    # באיזה שנה וחודש משתמש בשם "Roy Cundey" יצר חשבון (created), ובאיזה שנה וחודש הוא התחבר לאחרונה (last_login)
    user_roy_cundey = None
    for user in users:
        if user['first_name'] == 'Roy' and user['last_name'] == 'Cundey':
            user_roy_cundey = user

    user_roy_cundey_created_datetime = datetime.strptime(user_roy_cundey['created'], "%Y-%m-%dT%H:%M:%SZ")
    user_roy_cundey_created_at_year_and_month_string = datetime.strftime(user_roy_cundey_created_datetime, "Year: %Y, Month: %m")
    print(f'Roy Cundey created an account at- {user_roy_cundey_created_at_year_and_month_string}')

    user_roy_cundey_last_login_datetime = datetime.strptime(user_roy_cundey['last_login'], "%Y-%m-%dT%H:%M:%SZ")
    user_roy_cundey_last_login_year_and_month_string = datetime.strftime(user_roy_cundey_last_login_datetime,
                                                                         "Year: %Y, Month: %m")
    print(f'Roy Cundey last login was at- {user_roy_cundey_last_login_year_and_month_string}')

    # 3 -
    # כמה ימים עברו מאז ש"Easter Parmer" יצר את החשבון, לזמן שבו הוא התחבר לאחרונה
    user_easter_parmer = None
    for user in users:
        if user['first_name'] == 'Easter' and user['last_name'] == 'Parmer':
            user_easter_parmer = user

    user_easter_parmer_created_datetime = datetime.strptime(user_easter_parmer['created'], "%Y-%m-%dT%H:%M:%SZ")
    user_easter_parmer_last_login_datetime = datetime.strptime(user_easter_parmer['last_login'], "%Y-%m-%dT%H:%M:%SZ")
    how_many_days_passed_timedelta = user_easter_parmer_last_login_datetime - user_easter_parmer_created_datetime
    how_many_days_passed_string = how_many_days_passed_timedelta.days
    print(f'It has been {how_many_days_passed_string} days for Easter Parmer from last_login to created dates')


    # 4 -
    # אילו משתמשים לא התחברו בשלושה חודשים האחרונים ולכן אפשר ל"סמן אותם" כלא פעילים

    # 5 -
    # למצוא 3 משתמשים שיצרו חשבון הכי מוקדם, והתחברו בחודש האחרון
