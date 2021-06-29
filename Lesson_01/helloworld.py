# Calling print function with one string argument: 'Hello, World!'
# Functions can take 0 or more arguments (synonymous with "parameter"), separated by commas
# Argument or parameter refers to any input of a function
print("Hello World")

# You can call the print function with 0 arguments like so:
print()

# You can call the print function with multiple arguments separated by comma:
print("Hello World", "Hello Again")

# In these examples, we pass one or more String data types to the print function
# A String (shorthand: str) is a data type that represents ANY characters on your keyboard
# The syntax for a string is open quote, data, end quote. E.g. "hello"
# You can use double OR single quotes, but you can't mix and match

# Part 2

# Integers (shorthand: int) are a datatype that represent whole numbers (positive or negative)
# Floats (shorthand: float) are a datatype that represents decimal numbers (positive or negative)

# You can perform arithmetic in Python using built-in arithmetic "operators" (e.g. +, -, /, *, ...)
# The syntax (or grammar) for arithmetic expressions is number, operator, number. E.g. 1 + 2
print(1 + 2)

print(7 * 6)
print()

# If we pass multiple arguments to the print function, Python lets us combine data types
# Tip: Click a function and pres Ctrl+B to see the function definition
print("The end", "or is it?", "keep watching to learn more about Python", 3)

# input() built-in function will prompt the user for some input on the console
# input() can take 0 arguments, or 1 argument

# We can assign the input to a variable so we can do something with it later
# A variable is essentially a data container (i.e. a way to store any type of data)
user_input = input()

# We can use the print function to print out the input
# The input() function always returns a String
print(user_input)