from datetime import datetime, timedelta
import calendar
from collections import defaultdict


def get_users_list():
    file_name = 'data.txt'
    output_list = []
    temp_dict = dict()
    with open(file_name, 'r') as f:
        data = f.readlines()
        for i in data:
            name, birthday = i.replace('\n', '').split(',')
            temp_dict['name'] = name
            temp_dict['birthday'] = birthday
            output_list.append(temp_dict.copy())
    return output_list


def get_birthday_list():
    """    today_date = datetime(year=datetime.now().year,
                          month=datetime.now().month,
                          day=datetime.now().day)"""
    today_date = datetime(year=2022,
                          month=12,
                          day=2)

    day_step = timedelta(days=1)

    if today_date.weekday() == 5:
        iter_date = today_date
    elif today_date.weekday() > 5:
        iter_date = today_date - day_step
    else:
        iter_date = today_date + (5 - today_date.weekday()) * day_step

    users = get_users_list()
    output_list = defaultdict(list)
    for user in users:
        day, month, year = user['birthday'].split('.')
        user_birthday = datetime(year=int(year), month=int(month), day=int(day))
        for day in range(7):
            week_date = iter_date + timedelta(days=day)
            if (week_date.day == user_birthday.day) and (week_date.month == user_birthday.month):
                if user_birthday.weekday() == 5 or user_birthday.weekday() == 6:
                    output_list[0].append(user['name'])
                    continue
                output_list[user_birthday.weekday()].append(user['name'])

    return output_list


def get_pretty_birthday_list():
    users_list = get_birthday_list()
    output_str = ''
    for day, names in users_list.items():
        output_str += f'{calendar.day_name[day]}: '
        for name in names:
            output_str += f'{name}, '
        output_str = output_str[:-2]
        output_str += f'\n'
    return output_str


if __name__ == '__main__':
    print(get_pretty_birthday_list())

