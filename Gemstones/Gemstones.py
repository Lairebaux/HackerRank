"""
John has collected various rocks. Each rock has various minerals embedded in it. Each type of
mineral is designated by a lowercase letter in the range ascii[a-z] . There may be multiple
occurrences of a mineral in a rock. A mineral is called a gemstone if it occurs at least once in
each of the rocks in John's collection.
Given a list of minerals embedded in each of John's rocks, display the number of types of
gemstones he has in his collection.
"""

def gemstones(arr):
    subset = set(arr[0])
    for c in range(len(arr) - 1):
        subset &= set(arr[c + 1])
    return(len(subset))

