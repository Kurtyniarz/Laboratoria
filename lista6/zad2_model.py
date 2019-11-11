from datetime import datetime


def calc_diff(date_one, date_two):
    date_one = datetime.strptime(date_one, "%Y-%m-%d")
    date_two = datetime.strptime(date_two, "%Y-%m-%d")
    date_diff = abs((date_two - date_one).days)
    return print(f'Roznica dni: {date_diff}')
