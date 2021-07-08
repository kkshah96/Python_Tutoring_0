a = 11
b = 3

# This will print "2" because the remainder of 11 / 3 = 2
print(a % b)

type(a)
print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a // b)   # 4 integer division, truncates the decimal

print()

# We will go over for loops at a later time
for i in range(1, a // b):
    print(i)

# Booleans can have two values: True or False

# This variable would be equal to "False" because a is not 15
conditional = a == 15
print(conditional)

# If this "condition" succeeeds we will run all the code on the next indentation level
if a == 15:
    print('a is 15')
    print('finished conditional')
else:
    # Since a is not equal to 15, the "else" statement will run instead, and we will print "a is 11"
    # Note that three operations occur here: we convert a to a string, concatenate the resulting string to "a is ", and
    # then print the result
    print('a is ' + str(a))

# Next: learn about conditionals, loops, and more complex data structures (e.g. lists, tuples) in any order
