from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    date_now = datetime.now()
    date_plus_week = date_now + timedelta(weeks=1)-timedelta(days=1)
    week_days = ['Monday: ', 'Tuesday: ', 'Wednesday: ',
                 'Thursday: ', 'Friday: ', 'Saturday: ', 'Sunday: ']
    day_now = 7-date_now.weekday()
    monday = date_now.day+day_now

    users = {key: value.replace(year=2023) for key, value in users.items()}

    users2 = {key: value for key, value in users.items()
              if value < date_plus_week and value > date_now}

    if date_now.weekday() != 0:
        users3 = {key: value.replace(day=monday) for key, value in users2.items()
                  if value.weekday() == 6 or value.weekday() == 5}
        users2.update(users3)

    users = {key: value.weekday() for key, value in users2.items()
             if value.weekday() != 6 or value.weekday() != 5}

    for k in range(7):
        to_print = False
        for key, value in users.items():
            if value == k:
                to_print = True
                week_days[k] = week_days[k] + key + ', '
        if to_print:
            print(week_days[k][:-2])
