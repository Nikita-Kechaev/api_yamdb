import datetime


def current_year():
    return datetime.date.today().year


def range_year_validate(value):
    return -37000 <= value <= current_year()
