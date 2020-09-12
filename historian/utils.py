from datetime import datetime


def get_this_month():
    month = datetime.now()

    return month.strftime("%B")


def get_this_day():
    day = datetime.today()

    return day.day


def get_this_year():
    year = datetime.today()
    return year.year


def get_month_and_day():
    return f"{get_this_month()}_{get_this_day()}"


def get_full_date():
    return f"{get_this_day()} {get_this_month()} {get_this_year()}"