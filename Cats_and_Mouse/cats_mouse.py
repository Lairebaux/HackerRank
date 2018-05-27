"""
Two cats and a mouse are at various positions on a line. You will be given their starting
positions. Your task is to determine which cat will reach the mouse first, assuming the mouse
doesn't move and the cats travel at equal speed. If the cats arrive at the same time, the mouse
will be allowed to move and it will escape while the fight.
"""
def cats_and_mouse(x, y, z):
    a_check = abs(x - z)
    b_check = abs(y - z)
    if a_check == b_check:
        return "Mouse C"
    elif a_check < b_check:
        return "Cat A"
    else:
        return "Cat B"

