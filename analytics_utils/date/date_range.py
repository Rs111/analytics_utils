import datetime as dt
from typing import List
from . import validate


def date_range(date_start: str, date_end: str) -> List[str]:
    """Return a sequential list of dates between `date_start` and `date_end`."""

    if not type(date_start) == str or not type(date_end) == str:
        raise TypeError("one of the input dates is not a `str`")
    if not validate(date_start) or not validate(date_end):
        raise ValueError("one of the input dates is not in the '%Y-%m-%d' format")
    elif date_start > date_end:
        raise ValueError("date_start is greater-than date_end")
    else:
        datetime_start = dt.datetime.strptime(date_start, '%Y-%m-%d')
        datetime_end = dt.datetime.strptime(date_end, '%Y-%m-%d')
        timedelta = (datetime_end - datetime_start).days + 1

        incremental_datetimes = [datetime_start + dt.timedelta(days=i) for i in range(timedelta)]
        incremental_dates = list(map(lambda datetime: datetime.strftime("%Y-%md-%d"), incremental_datetimes))
        return incremental_dates
