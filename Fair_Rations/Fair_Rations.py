"""
You are the benevolent ruler of Rankhacker Castle, and today you're distributing bread. Your
subjects are in a line, and some of them already have some loaves.
Times are hard and your castle's food stocks are dwindling, so you must distribute as few
loaves as possible according to the following rules:

1. Every time you give a loaf of bread to some person , you must also give a loaf of bread to
the person immediately in front of or behind them in the line (i.e., persons i + 1 or i - 1).

2. After all the bread is distributed, each person must have an even number of loaves.
Given the number of loaves already held by each citizen, find and print the minimum number
of loaves you must distribute to satisfy the two rules above. If this is not possible, print NO.

For example, the people in line have loaves B = [4,5,6,7].
We can first give a loaf to i = 3 and i = 4 so B = [4,5,7,8].
Next, we give a loaf to i = 2 and i = 3 and i = 4 so B = [4,6,8,8]
which satisfies our conditions. We had to distribute loaves
"""

def fair_rations(B):
    count = 0
    if sum(B) % 2 != 0:
        return "NO"
    else:
        for num in range(len(B)):
            if B[num] % 2 != 0:
                B[num] += 1
                B[num + 1] += 1
                count += 2
    return count


