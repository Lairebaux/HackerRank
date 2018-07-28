"""
Assume you are given the array indexed arr = [1,2,4,5,3] indexed 0...4.
Store the value of arr[4]
Now test lower index values successively 3 to 0
until you reach a value that is lower
than arr[4], arr[1] in this case.
Each time your test fails,
copy the value at the lower index to
the current index and print your array.
When the next lower indexed value is smaller than
arr[4], insert the stored value at the current index and print the entire array.
The results of operations on the example array is:
Starting array: [1,2,4,5,3]
Store the value of arr[4] = 3 Do the tests and print interim results:

1 2 4 5 5
1 2 4 4 5
1 2 3 4 5

"""
def insertion_sort_1(n, arr):
    for i in range(n):
        target = arr[i]
        pos = i
        while pos > 0 and target < arr[pos - 1]:
            arr[pos] = arr[pos - 1]
            print(" ".join(str(num) for num in arr))
            pos -= 1
            arr[pos] = target
    print(" ".join(str(num) for num in arr))


