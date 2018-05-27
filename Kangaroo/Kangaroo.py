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
    if v2 == v1 or v2 > v1:
        return "NO"
    elif (x1- x2) % (v2 - v1) == 0:
        return "YES"
    else:
        return "NO"




