# NOTE: Conditionals and Loops practice problems
# https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

# 1. Write a Python program to find the numbers that are divisible by 7 and also divisible by 5
# between 1500 and 2700 (both included)

# NOTE: How to check if num2 is divisible by num1
num1 = 5
num2 = 10

if num2 % num1 == 0:
    print(f"{num2} is divisible by {num1}")

# Q1 Solution
for num3 in range(1500, 2701):
    if num3 % 7 == 0 and num3 % 5 == 0:
        print(num3)

# 2. Write a Python program which iterates the integers from 1 to 50.
# For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

# Q2 Solution
for num4 in range(1, 51):
    if num4 % 3 == 0 and num4 % 5 != 0:
        print("Fizz")
    elif num4 % 5 == 0 and num4 % 3 != 0:
        print("Buzz")
    elif num4 % 3 == 0 and num4 % 5 == 0:
        print("FizzBuzz")
    else:
        print(num4)

# A slightly more efficient solution:
for num4 in range(1, 51):
    if num4 % 3 == 0 and num4 % 5 == 0:
        print("FizzBuzz")
    elif num4 % 3 == 0:
        print("Fizz")
    elif num4 % 5 == 0:
        print("Buzz")
    else:
        print(num4)

