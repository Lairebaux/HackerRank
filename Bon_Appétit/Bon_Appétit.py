"""
Anna and Brian are sharing a meal at a restaurant and they agree to split the bill equally. Brian
wants to order something that Anna is allergic to though, and they agree that Anna won't pay
for that item. Brian gets the check and calculates Anna's portion. You must determine if his
calculation is correct

You are given an array of prices, , the cost of each of the items, , the item Anna doesn't
eat, and , the total amount of money that Brian charged Anna for her portion of the bill. If the
bill is fairly split, print Bon Appétit. Otherwise, print the integer amount of money that Brian
must refund to Anna.
"""

def bon_appetit(items, index, expected):
    unwanted = items.pop(index)
    total = sum(items) // 2
    refund = unwanted // 2
    if total == expected:
        return "Bon Appetit"
    return refund



