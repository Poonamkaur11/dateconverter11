import datetime
import calendar
from datetime import date, timedelta
#from dateutil.rrule import rrule, MONTHLY, FR


def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    return next_month - datetime.timedelta(days=next_month.day)


def sat_of_next_month():
    last_day = last_day_of_month(datetime.datetime.now())
    return next_weekday(last_day, 5)


def day_after_tom():
    return datetime.datetime.now() + datetime.timedelta(days=2)


def tom():
    return datetime.datetime.now() + datetime.timedelta(days=1)


def next_sat():
    d = datetime.datetime.now()
    return d + datetime.timedelta((12 - d.weekday()) % 7)


def next_week_sat():
    return next_weekday(datetime.datetime.now(), 5)


def next_wed():
    d = datetime.datetime.now()
    return d + datetime.timedelta((9 - d.weekday()) % 7)


def two_days_before_xmas():
    return datetime.datetime.strptime('2312{year}'.format(year=str(datetime.date.today().year)), "%d%m%Y").date()


def two_days_after_xmas():
    return datetime.datetime.strptime('2712{year}'.format(year=str(datetime.date.today().year)), "%d%m%Y").date()


dict_map = {
    'sat_of_next_month': sat_of_next_month,
    'day_after_tom': day_after_tom,
    'tom': tom,
    'next_wed': next_wed,
    'next_sat': next_sat,
    'next_week_sat': next_week_sat,
    'two_days_before_xmas': two_days_before_xmas,
    'two_days_after_xmas': two_days_after_xmas
}