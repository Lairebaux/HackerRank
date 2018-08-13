"""

HackerLand University has the following grading policy:
Every student receives a in the inclusive range 0 from to 100.
Any grade less than 40 is a failing grade.

Sam is a professor at the university and likes to round each student's grade according to
these rules:

If the difference between the grade and the next multiple of 5 is less than 3,
round grade up to the next multiple of 5.

If the value of grade is less than 38,
no rounding occurs as the result will still be a failing grade.

For example, grade = 84 will be rounded to 85 but grade = 29 will not be rounded
because the rounding would result in a number that is less than 40.

Given the initial value of for each of Sam's students,
write code to automate the rounding process.

Complete the function solve that takes an integer array of all grades, and
return an integer array consisting of the rounded grades.
For each grade, round it according
to the rules above and print the result on a new line.

The first line contains a single integer denoting n (the number of students).
Each line of the subsequent lines contains a single integer, grade-i,
denoting student i's grade.
"""


def grading_students(grades):
    for i in grades:
        if i % 5 >= 3 and i >= 38:
           print(i + 5 - i % 5)
        else:
            print(i)





if __name__ == '__main__':
    # n = int(input())
    grades = [73,67,38,33]
    # for _ in range(n):
    #     grades_item = int(input())
    #     grades.append(grades_item)
    result = grading_students(grades)
    # print('\n'.join(map(str, result)))
    # print(result)