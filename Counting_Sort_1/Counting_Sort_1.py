"""
Given a list of integers, count and output the number of times each value appears as a list of
space-separated integers


The first line contains an integer n, the number of items in arr.
Each of the next n lines contains an integer arr[i] where 0 <= i < n.
"""


def counting_sort_1(arr):
    counter = [0] * 100
    for i in arr:
        counter[i] += 1
    return counter


if __name__ == '__main__':
    # n = 5
    # arr = [1,1,3,2,1]
    # arr = [50,0, 13,99, 99, 50, 20,
    #        0 ,1 ,3 ,5, 50, 1, 10, 15]
    arr = []
#     # n = int(input())
    # arr = list(map(int, input().rstrip().split()))
    result = counting_sort_1(arr)
    print(result)

