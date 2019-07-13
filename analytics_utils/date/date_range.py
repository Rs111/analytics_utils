import datetime as dt
from typing import List, Tuple
from analytics_utils.date.days import add_days
from analytics_utils.date.validate import validate


def date_range(date_start: str, date_end: str, date_format: str = "%Y-%m-%d") -> List[str]:
    """Return a sequential list of dates between `date_start` and `date_end`"""

    assert validate(date_start, date_format), "date_start must be of valid '{0}' format".format(date_format)
    assert validate(date_end, date_format), "date_end must be of valid '{0}' format".format(date_format)

    datetime_start = dt.datetime.strptime(date_start, date_format)
    datetime_end = dt.datetime.strptime(date_end, date_format)
    assert datetime_start <= datetime_end, "date_start must be lesser-than-or-equal-to date_end"
    timedelta = (datetime_end - datetime_start).days + 1

    datetime_list = [datetime_start + dt.timedelta(days=i) for i in range(timedelta)]
    date_list = list(map(lambda datetime: datetime.strftime(date_format), datetime_list))
    return date_list


def date_range_with_weeks(date_start: str, date_end: str, date_format: str = "%Y-%m-%d") -> List[Tuple]:
    """Returns same output as :function:`date_range`, but also includes week start/end values for each date"""

    date_list = date_range(date_start, date_end, date_format)
    datetime_list = [dt.datetime.strptime(date, date_format) for date in date_list]
    datetime_start = dt.datetime.strptime(date_start, date_format)

    add_wk_st = [((datetime - datetime_start).days // 7) * 7 for datetime in datetime_list]
    add_wk_ed = [i + 6 for i in add_wk_st]

    return [(date, add_days(date_start, i), add_days(date_start, j)) for (date, i, j) in
            zip(date_list, add_wk_st, add_wk_ed)]
