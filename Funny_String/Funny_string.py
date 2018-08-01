"""
In this challenge, you will determine whether a string is funny or not.
 determine whether a
string is funny, create a copy of the string in reverse e.g. abc->cba .
Iterating through each
string, compare the absolute difference in the ascii values of the
characters at positions 0 and
1, 1 and 2 and so on to the end. If the list of absolute differences
is the same for both strings,
they are funny.
Note: The absolute value of x, is written as |x|.
Input Format
The first line contains an integer , (the number of test cases).
The next lines contain a string, .

"""
def funny_string(s):
    pos = 0
    while pos < len(s) // 2:
        head = abs(ord(s[pos]) - ord(s[pos + 1]))
        tail = abs(ord(s[~pos]) - ord(s[~pos - 1]))
        if head != tail:
            return "Not Funny"
        pos += 1
    return "Funny"


if __name__ == '__main__':

    q = int(input())
    for q_itr in range(q):
        s = input()
        result = funny_string(s)
        print(result)
