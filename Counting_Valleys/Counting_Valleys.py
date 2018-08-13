"""
Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details
like topography. During his last hike, he took exactly n steps. For every step he took, he noted
if it was an uphill, U, D or a downhill, step. Gary's hikes start and end at sea level and each
step up or down represents a 1 unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level,
starting with a step up from
sea level and ending with a step down to sea level.

A valley is a sequence of consecutive steps below sea level,
starting with a step down from
sea level and ending with a step up to sea level.

Given Gary's sequence of up and down steps during his last hike,
find and print the number of
valleys he walked through.

For example, if Gary's path is s = [DD UUUU DD]
he first enters a valley 2 units deep.

Then he climbs out an up onto a mountain 2 units high.
Finally, he returns to sea level and
ends his hike.
_/\      _
   \    /
    \/\/

The first line contains an integer n, the number
of steps in Gary's hike.
The second line contains a single string s,
of n characters describing his path.

Print a single integer denoting the number of valleys
Gary walked through during his hike.
"""


def counting_valleys(n, s):
    count = valley = 0
    for step in range(n):
        if s[step] == "U":
            count += 1
        else:
            count -= 1
        if s[step] == "U" and count == 0:
            valley += 1
    return valley


