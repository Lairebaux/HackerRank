"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
Note: Midnight is 12:00:00AM on a 12-hour clock,
and 00:00:00 on a 24-hour clock. Noon is
12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
"""


def time_conversion(s):
    hours, mins, secs = s.split(":")
    print(hours,mins,secs)
    secs = secs[:2]
    if  "AM" in s and hours == '12':
        hours = int(hours) - 12
        return "{:02}:{}:{}".format(hours,mins,secs)
    elif 'PM' in s and hours != '12':
        hours = int(hours) + 12
        return "{:02}:{}:{}".format(hours,mins,secs)
    else:
        return "{}:{}:{}".format(hours,mins,secs)
