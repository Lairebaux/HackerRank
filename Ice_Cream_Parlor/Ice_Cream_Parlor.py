"""
Sunny and Johnny like to pool their money and go to the ice cream parlor. Johnny never buys
the same flavor that Sunny does. The only other rule they have is that they spend all of their
money.
Given a list of prices for the flavors of ice cream, select the two that will cost all of the money
they have.
Complete the function iceCreamParlor below to return an array containing the indexes of the
prices of the two flavors they buy. The returned array must be sorted ascending
"""

def ice_cream_parlor(f, m):
    checker = {}
    for num in range(len(f)):
        diff = m - f[num]
        if diff in checker:
            return checker[diff] + 1, num + 1
        checker[f[num]] = num

