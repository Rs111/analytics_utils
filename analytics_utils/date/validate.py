import datetime as dt


def validate(date: str, date_format: str = "%Y-%m-%d") -> bool:
    """Indicates whether `date` is of `date_format`.

    :param date: date to be evaluated
    :param date_format: format against which to evaluate date (see: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)
    :return: whether `date` is of `format`
    """

    try:
        parsed = dt.datetime.strptime(date, date_format).strftime(date_format)
        return date == parsed
    except ValueError:
        return False
