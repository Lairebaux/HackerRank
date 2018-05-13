"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
Note: Midnight is 12:00:00AM on a 12-hour clock,
and 00:00:00 on a 24-hour clock. Noon is
12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
"""


def time_conversion(s):
    am_pm, blank = "AMPM", "    "
    table = str.maketrans(am_pm, blank)
    remove_am_pm = s.translate(table)
    no_colon = remove_am_pm.strip().split(":")
    hours, mins, secs = [num for num in no_colon]
    if "AM" in s and hours == '12':
        hours = int(hours) - 12
        return f"0{hours}:{mins}:{secs}"
    elif "PM" in s and hours != "12":
        hours = int(hours) + 12
        return f"{hours}:{mins}:{secs}"
    else:
        return f"{hours}:{mins}:{secs}"

