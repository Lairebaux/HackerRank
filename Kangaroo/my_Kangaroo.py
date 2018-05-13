"""
You are choreographing a circus show with various animals. For one act, you are given two
kangaroos on a number line ready to jump in the positive direction (i.e, toward positive
infinity).
The first kangaroo starts at location x1 and moves at a rate v1 of meters per jump.
The second kangaroo starts at location x2 and moves at a rate v2 of meters per jump.
You have to figure out a way to get both kangaroos at the same location as part of the show.
Create function kangaroo which takes starting location and speed of both kangaroos
as input, and return YES or NO appropriately. Can you determine if the kangaroos will ever
land at the same location at the same time? The two kangaroos must land at the same
location after making the same number of jumps.
"""

def kangaroo(x1, v1, x2, v2):
    distance = v1 * x2
    num_of_jumps_x1 = (v1 * distance) - distance
    num_of_jumps_x2 = v2 * distance
    if num_of_jumps_x1 == num_of_jumps_x2:
        return "YES"
    return "NO"


