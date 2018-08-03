"""
Lily likes to play games with integers. She has created a new game where she
determines the difference between a number and its
reverse.

For instance, given the number 12, its reverse is 21. Their difference is 9 .
The number 120 reversed is 21, and their difference is 99.
.
She decides to apply her game to decision making. She will look at a numbered
range of days and will only go to a movie on a beautiful
day.

Given a range of numbered days,[i...j] and a number k, determine the number of day
s in the range that are beautiful.

Beautiful numbers are defined as numbers where |i - reverse(i)| is evenly divisible by k.
If a day's value is a beautiful number, it is a beautiful day.

Print the number of beautiful days in the range.

A single line of three space-separated integers
describing the respective values of i, j, and k.
"""

def beautiful_days(i, j, k):
    n = 0
    for num in range(i, j):
        if abs(num - int(str(num)[::-1])) % k == 0:
            n += 1
    return n





if __name__ == '__main__':
    ijk = input().split()
    i = int(ijk[0])
    j = int(ijk[1])
    k = int(ijk[2])
    result = beautiful_days(i, j, k)
    print(str(result) + '\n')

