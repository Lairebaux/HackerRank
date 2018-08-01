"""
Numeros the Artist had two lists that were permutations of one another. He was very proud.
Unfortunately, while transporting them from one exhibition to another, some numbers were
lost out of the first list. Can you find the missing numbers?
Notes
If a number occurs multiple times in the lists, you must ensure that the frequency of that
number in both lists is the same. If that is not the case, then it is also a missing number.
You have to print all the missing numbers in ascending order.
Print each missing number once, even if it is missing multiple times.
The difference between maximum and minimum number in the second list is less than or
equal to 100.

There will be four lines of input:

arr size of list-n
i1 i2 i3 ...
brr size of 2e list-m
i1 i2 i3 ...


"""
def missing_numbers(arr, brr):
    arr_count = [0] * 101
    brr_count = [0] * 101
    nums = []
    diff = min(brr)
    for n in brr:
        brr_count[n - diff] += 1
    for n in arr:
        arr_count[n - diff] += 1
    for pos in range(101):
        if brr_count[pos] != arr_count[pos]:
            nums.append(pos + diff)
    return nums

