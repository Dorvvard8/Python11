from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    result_list = []
    date_now = datetime.now()
    date_plus_week = date_now + timedelta(weeks=1)-timedelta(days=1)
    week_days = ['Monday: ', 'Tuesday: ', 'Wednesday: ',
                 'Thursday: ', 'Friday: ', 'Saturday: ', 'Sunday: ']
    day_now = 7-date_now.weekday()
    monday = date_now.day+day_now
    k = 0
    for user_item in users:
        birthday = user_item['birthday']
        birthday = birthday.replace(year=2023)
        if birthday > date_plus_week or birthday < date_now-timedelta(days=1):
            continue
        if birthday.weekday() == 6 or birthday.weekday() == 5:
            birthday = birthday.replace(day=monday)
        day_week_int = int(birthday.weekday())
        week_days[day_week_int] = week_days[day_week_int] + \
            str(user_item['name'] + ', ')
        k += 1
    for i in range(5):
        if week_days[i][-2] != ':':
            print(week_days[i][:-2])


# users = list()
# users = [
#     {'name': 'Sveta', 'birthday': datetime(year=2001, month=2, day=6)},    # Monday
#     {'name': 'Dima', 'birthday': datetime(year=2001, month=2, day=7)},     # Tuesday
#     {'name': 'Vasia', 'birthday': datetime(year=2001, month=2, day=8)},    # Wednesday
#     {'name': 'Kolia', 'birthday': datetime(year=1995, month=2, day=9)},    # Thursday
#     {'name': 'Maria', 'birthday': datetime(year=1998, month=2, day=9)},    # Thursday
#     {'name': 'Slava', 'birthday': datetime(year=2004, month=2, day=10)},   # Friday
#     {'name': 'Galina', 'birthday': datetime(year=2004, month=2, day=11)},  # Saturday
#     {'name': 'Natali', 'birthday': datetime(year=2005, month=2, day=12)},  # Sunday
#     {'name': 'Serg', 'birthday': datetime(year=2001, month=2, day=13)},    # Monday
#     {'name': 'Misha', 'birthday': datetime(year=1997, month=2, day=14)},   # Tuesday
#     {'name': 'Kostia', 'birthday': datetime(year=2003, month=2, day=15)}   # Wednesday
# ]


get_birthdays_per_week(users)
