"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
Note: Midnight is 12:00:00AM on a 12-hour clock,
and 00:00:00 on a 24-hour clock. Noon is
12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
"""

def time_conversion(s):
    am_pm = s[-2:]
    hours, mins, secs = s[:-2].split(":")
    if "AM" == am_pm and hours == "12":
        hours = "00"
    if "PM" == am_pm and hours != "12":
        hours = str(int(hours) + 12)
    return "{}:{}:{}".format(hours, mins, secs)


