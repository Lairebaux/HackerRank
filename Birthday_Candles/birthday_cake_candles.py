"""You are in-charge of the cake for your niece's birthday and have decided the cake will have
one candle for each year of her total age. When she blows out the candles, she’ll only be able
to blow out the tallest ones. Your task is to find out how many candles she can successfully
blow out.
"""

def birthday_cake_candles(n, ar):
    ar = sorted(ar)
    half_list = ar[n // 2: - 1]
    return ar.count(max(half_list))

