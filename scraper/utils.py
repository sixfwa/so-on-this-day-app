from datetime import datetime


def get_this_month():
    month = datetime.now()

    return month.strftime("%B")


def get_this_day():
    day = datetime.today()

    return day.day
