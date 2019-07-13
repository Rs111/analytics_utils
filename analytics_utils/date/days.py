import datetime as dt
from analytics_utils.date import validate


def add_days(date: str, days: int, date_format: str = "%Y-%m-%d") -> str:
    """add `days` to date"""
    assert validate(date, date_format), "date must be of valid '{0}' format".format(date_format)
    datetime = dt.datetime.strptime(date, date_format) + dt.timedelta(days=days)

    return datetime.strftime(date_format)


def minus_days(date: str, days: int, date_format: str = "%Y-%m-%d") -> str:
    """subtract `days` from `date`"""
    return add_days(date, -days, date_format)


def add_weeks(date: str, weeks: int, date_format: str = "%Y-%m-%d") -> str:
    """add `weeks` to `date`"""
    return add_days(date, weeks*7, date_format)


def minus_weeks(date: str, weeks: int, date_format: str = "%Y-%m-%d") -> str:
    """subtract `weeks` from `date`"""
    return add_days(date, -weeks*7, date_format)
