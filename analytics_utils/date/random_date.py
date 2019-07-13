import datetime as dt
from random import randint
from analytics_utils.date import validate


def random_date(date_start: str, date_end: str, date_format: str = "%Y-%m-%d") -> str:
    """Return a random date between `date_start` and `date_end`"""

    assert validate(date_start, date_format), "date_start must be of valid '{0}' format".format(date_format)
    assert validate(date_end, date_format), "date_end must be of valid '{0}' format".format(date_format)

    datetime_start = dt.datetime.strptime(date_start, date_format)
    datetime_end = dt.datetime.strptime(date_end, date_format)
    assert datetime_start <= datetime_end, "date_start must be lesser-than-or-equal-to date_end"

    random_timedelta = randint(0, (datetime_end - datetime_start).days)
    date = (datetime_start + dt.timedelta(days=random_timedelta))

    return date.strftime(date_format)
