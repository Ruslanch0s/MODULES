from datetime import datetime


def format_datetime(value, format="%Y.%m.%d | %H:%M"):
    if isinstance(value, datetime):
        return value.strftime(format)
    return value


def format_time(value, format="%H:%M"):
    if isinstance(value, datetime):
        return value.strftime(format)
    return value

# Используйте 'value' для корректного формата
