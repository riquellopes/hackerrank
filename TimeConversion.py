"""
    >>> timeConversion("07:05:45PM")
    '19:05:45'
    >>> timeConversion("06:20:45PM")
    '18:20:45'
    >>> timeConversion("12:20:45PM")
    '12:20:45'
    >>> timeConversion("06:20:45AM")
    '06:20:45'
    >>> timeConversion("12:00:00AM")
    '00:00:00'
    >>> timeConversion("12:40:22AM")
    '00:40:22'
"""


def timeConversion(s):
    hours, minutes_and_seconds = s[:2], s[2:8]
    if "PM" in s:
        hours = int(hours)
        if hours != 12:
            hours = hours + 12
        hours = hours if hours < 24 else '00'
    elif "12" == s[:2] and "AM" in s:
        hours, minutes_and_seconds = "00", s[2:8]
    return "{}{}".format(hours, minutes_and_seconds)
