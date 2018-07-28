"""
Little Bobby loves chocolate. He frequently goes to his favorite  5 & 10 store, Penny Auntie, to
buy them. They are having a promotion at Penny Auntie. If Bobby saves enough wrappers, he
can turn them in for a free chocolate.

The first line contains an integer, t , denoting the number of scenarios to analyze.
n = money to spend,
c = cost of a chocolate,
m =  number of wrappers he can turn in for a free chocolate.

t = 3
10 2 5
12 4 4
6 2 2

return the number of chocolates Bobby can eat with a given
amount of money after taking full advantage of the promotion.
"""

def chocolate_feast(n, c, m):
    chocs = n // c
    wrappers = chocs
    while wrappers >= m:
        free_choc = wrappers // m
        wrappers = free_choc + (wrappers % m)
        chocs += free_choc
    return chocs

