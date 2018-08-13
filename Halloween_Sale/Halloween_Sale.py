"""
You wish to buy video games from the famous online video game store Mist.
Usually, all games are sold at the same price, p dollars. However, they are planning to have
the seasonal Halloween Sale next month in which you can buy games at a cheaper price.

The first game you buy during the sale will be sold at p dollars,
every subsequent game you buy will be sold at exactly d dollars
less than the cost of the previous one.

This will continue until the cost becomes less than or equal to m dollars
after which every game you buy will cost m dollars each.

For example, if p = 20, d = 3 and m = 6,
then the following are the costs of the first 11 games you buy, in order:

20,17,14,11,8,6

You have dollars in your Mist wallet.
How many games can you buy during the Halloween Sale?

s = total amount of money
p = first game
d = dollars less than or equal to m dollars
m = cost of every game after
"""
def how_many_games(p, d, m, s):
    games = 0
    while s >= 0:
        s -= p
        p = max(p - d, m)
        games += 1
    return games - 1


