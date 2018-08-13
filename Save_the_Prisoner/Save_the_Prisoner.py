"""
A jail has a number of prisoners and a number of treats to pass out to them.

Their jailer decides the fairest way to divide
the treats is to seat the prisoners around a circular table in
sequentially numbered chairs.

A chair number will be drawn from a hat.

Beginning with the prisoner in that chair, one candy will be handed
to each prisoner sequentially around table until all have been distributed.

The jailer is playing a little joke, though.

The last piece of candy looks like all the others, but it
tastes awful.

Determine the chair number occupied by the prisoner who will receive that candy.

t = test cases

n = the number of prisoners
s = the chair number to start passing out treats at
m = the number of sweets

For each test case, print the chair number of the prisoner who receives the awful treat on a
new line.
"""

def save_the_prisoner(n, s, m):
    return (s + m - 2) % n + 1

