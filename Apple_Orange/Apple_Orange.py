def count_apples_and_oranges(s, t, a, b, apples, oranges):
    print(len([1 for x in apples if s <= (x + a) <= t]))
    print(len([1 for x in oranges if s <= (x + b) <= t]))

