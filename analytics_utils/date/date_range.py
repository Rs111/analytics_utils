import datetime as dt
from . import validate

def date_range(date_start, date_end):
    """Return a sequential list of date strings of all dates between the input start and end parameters"""
    if not validate(date_start) or not validate(date_end):
        raise ValueError("one of the input dates is not a valid '%Y-%m-%d' date String")
    elif date_start > date_end:
        raise ValueError("date_start is greater-than date_end")
    else:
        datetime_start = dt.datetime.strptime(date_start, '%Y-%m-%d')
        datetime_end = dt.datetime.strptime(date_end, '%Y-%m-%d')
        timedelta = (datetime_end - datetime_start).days + 1

        incremental_datetimes = [datetime_start + dt.timedelta(days=i) for i in range(timedelta)]
        incremental_dates = list(map(lambda datetime: datetime.strftime("%Y-%md-%d"), incremental_datetimes))
        return incremental_dates
