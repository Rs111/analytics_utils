import datetime as dt


def validate(date, format):
    """Indicates whether date matches format

    :param date: date String to be evaluated
    :param format: format String against which to evaluate date (see: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)
    :return: Boolean indicating whether date matches format
    """
    try:
        parsed = dt.datetime.strptime(date, format).strftime(format)
        return date == parsed
    except ValueError:
        return False


def validate(date):
    """Overloaded version of the function above with the format parameter set to '%Y-%m-%d'"""
    try:
        parsed = dt.datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d')
        return date == parsed
    except ValueError:
        return False