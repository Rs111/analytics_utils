import datetime as dt

def validate(date, date_format = "%Y-%m-%d"):
    """Indicates whether date matches format

    :param date: date String to be evaluated
    :param format: format String against which to evaluate date (see: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)
    :return: Boolean indicating whether date matches format
    """
    try:
        parsed = dt.datetime.strptime(date, date_format).strftime(date_format)
        return date == parsed
    except ValueError:
        return False
