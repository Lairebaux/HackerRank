"""

3
11 2  4
4  5  6
10 8  -12

Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15

Print the absolute difference between the sums of the matrix's two diagonals as a single
integer
"""

def diagonal_difference(a):
    diff = 0
    for num in range(len(a)):
        diff += a[num][num]
        diff -= a[num][len(a) - num - 1]
    return abs(diff)

