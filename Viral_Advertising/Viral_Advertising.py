"""
HackerLand Enterprise is adopting a new viral advertising strategy.
When they launch a new
product, they advertise it to exactly people 5 on social media.
On the first day, half of those people (i.e., 5//2 = 2 )
like the advertisement and each shares it with of their friends.
At the beginning of the second day,
(5//2) x 3 = 6 people receive the advertisement.
Each day, n(recipients)//2 of the recipients like the advertisement
and will share it with friends on the following day.
Assuming nobody receives the advertisement twice,
determine how many people have liked the ad by the end of a given day,
beginning with launch day as day .
"""


def viral_advertising(n):
    cumulative = 0
    promote = 5
    for _ in range(n):
        liked = promote // 2
        shared = liked * 3
        cumulative += liked
        promote = shared
    return cumulative
