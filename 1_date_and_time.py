"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dt_now = datetime.now()
    dt_yesterday = dt_now - timedelta(days=1)
    dt_month_ago = dt_now - timedelta(days=30)

    print("вчера -", dt_yesterday.strftime('%Y-%m-%d'), 
          "сегодня -", dt_now.strftime('%Y-%m-%d'), 
          "30 дней назад -", dt_month_ago.strftime('%Y-%m-%d'))

def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_string = '01/01/20 12:10:03.234567'
    date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
    return date_dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
