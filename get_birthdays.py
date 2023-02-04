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

    # users2 = {key: value.replace(year=2023) for key, value in users.items()
    #           if value.replace(year=2023) < date_plus_week}
    # print('\nusers3 : ', users)
    # users.update(users2)
    #
    # users.update(users2)
    # print('\nusers : ', users)
    # return result
# quantity — количество чисел в наборе(должен быть min < quantity < max)
users = dict()
Dima = datetime(year=2001, month=2, day=3)
Vasia = datetime(year=2001, month=2, day=4)
Kolia = datetime(year=1995, month=2, day=5)
Slava = datetime(year=2004, month=2, day=6)
Galina = datetime(year=2004, month=2, day=7)
Sveta = datetime(year=2001, month=2, day=8)
Natali = datetime(year=2005, month=2, day=9)
Serg = datetime(year=2001, month=2, day=10)
Misha = datetime(year=1997, month=2, day=11)
Kostia = datetime(year=2003, month=2, day=12)
Maria = datetime(year=1998, month=2, day=13)
users = {'Dima': Dima, 'Vasia': Vasia, 'Kolia': Kolia, 'Slava': Slava, 'Galina': Galina, 'Sveta': Sveta,
         'Natali': Natali, 'Serg': Serg, 'Misha': Misha, 'Kostia': Kostia, 'Maria': Maria}
get_birthdays_per_week(users)
