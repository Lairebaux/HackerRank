"""
John Watson knows of an operation called a right circular rotation on an array of integers. One
rotation operation moves the last array element to the first position and shifts all remaining
elements right one. To test Sherlock's abilities, Watson provides Sherlock with an array of
integers. Sherlock is to perform the rotation operation a number of times then determine the
value of the element at a given position.
For each array, perform a number of right circular rotations and return the value of the
element at a given index.

For example, array a = [3,4,5], k = 2 and m = [1,2] .
First we perform the two rotation
[3,4,5] -> [5,3,4] -> [4,5,3]

Now return the values from indexes 1 and 2 as indicated in the m array.
a[1] = 5 , a[2] = 3

The first line contains space-separated integers:
n k q
n = the number of elements in the integer array
k = rotation count
q = the number of queries.

The second line contains space-separated integers, where each integer i describes array
element a[1]( where 0 <=i<=n)

Each of the q subsequent lines contains a single integer denoting m, the index of the element
to return from a.

3 2 3
1 2 3
0
1
2
"""

def circular_array_rotation(a, k, queries):
    x = []
    for i in range(len(a)):
        x.append(a[(i - k) % len(a)])
    return [x[j] for j in queries]


