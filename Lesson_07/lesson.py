# Problem: Have the user guess a number. Print if it's too low or too high, and give them 2 total chances to guess.
num = 10

# Iteration 1:
guess = int(input("Enter a number: "))

if guess < num:
	print('Too low. Guess again.')
	guess = int(input())
	if gues != num:
		print('You lose')
	else:
		print('You win')
elif guess > num:
	print('Too high. Guess again.')
	guess = int(input())
	if guess != num:
		print('You lose')
else:
	print('You win')


# Note: We notice that there is a lot of duplicated code. Let's see if we can combine the "if" and "elif" block to reduce duplication
# Iteration 2
guess = int(input("Enter a number: "))

if guess != num:
	if guess < num:
		print('Too low. Guess again.')
	elif guess > num:
		print('Too high. Guess again.')
	guess = int(input())
	if guess != num:
		print('You lose')
	else:
		print('You win')
else:
	print('You win')

# Iteration 3 
# A small optimization we can make by removing a redundant conditional
guess = int(input("Enter a number: "))

if guess != num:
	if guess < num:
		print('Too low. Guess again.')
	else:
		print('Too high. Guess again.')
	guess = int(input())
	if guess != num:
		print('You lose')
	else:
		print('You win')
else:
	print('You win')

# LISTS

# Lists are denoted by square brackets. The below would create an empty list
my_empty_list = []

# Lists can contain any number of data points of any type, where data points are separated by commas
my_list_of_things = ['hello', 'abc', 123, 5.0, False]

# We can index or slice lists the same way we index or slice strings
my_list_of_things[4] # => False
my_list_of_things[1:3] # => ['abc', 123]

# We can get the length of a list using the python built-in function len()
len(my_list_of_things) # => 5

# We can add items to the end of a list using the .append() function, which will directly modify the list
my_list_of_things.append('new_thing')
# The length of the list increases because it now also contains "new_thing"
len(my_list_of_things) # => 6

# Lists can reference functions (Note: this is not usually done in practice!!)
def my_function():
	print('hello world')

new_list = [my_function]
my_list_of_things[0]() # => This will print 'hello world'

# OBJECTS

# Objects in Python and almost all other programming languages refer to collections of data and functions.
# i.e. .append() is a function that the Python "list" object contains (and can thereby only be called on lists). The actual data would be whatever we put in the square brackets upon defining the list
