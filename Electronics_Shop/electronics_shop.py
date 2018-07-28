"""
Monica wants to buy a keyboard and a USB drive from her favorite electronics store. The store
has several models of each. Monica wants to spend as much as possible for the items, given
her budget.
Given the price lists for the store's keyboards and USB drives, and Monica's budget, find and
print the amount of money Monica will spend. If she doesn't have enough money to both a
keyboard and a USB drive, print -1 instead. She will buy only the two required items.
For example, suppose she has s=60 to spend. Three types of keyboards
keyboards = [40,50,60]. Two USB drives cost drives = [5,8,12] She could purchase a
40 + keyboard + 12 usb drive = 52 or a keyboard + 8 usb drive = 58.
She chooses the latter. She can't buy more than 2 items so she can't spend exactly 60.
"""


def get_money_spent(keyboards, drives, budget):
    keyboards = sorted(keyboards, reverse=True)
    drives = sorted(drives)
    wallet = -1
    for k_items in keyboards:
        for d_items in drives:
            if k_items + d_items > budget:
                break
            elif k_items + d_items > wallet:
               wallet = k_items + d_items
    return wallet







