# Functions are defined using the "def" keyword, followed by name we assign to the function, and then in parantheses, a list of "arguments" the function accepts
# E.g. def my_function(arg1, arg2, ...)

# Defining a function to add two numbers together and return the result:
def add_nums(num1, num2):
  result = num1 + num2
  return result

result = add_nums(5, 7)
print(result) # => 12

print(add_nums(1, "hello"))

# Notes:
# 1. "num1", "num2", and "result" do not actually exist until the function is later called. They can be thought of as "placeholders"
# 2. For the reason above, the "result" defined on line 9 will not conflict with the result defined on line 6. The "result" on line 6 only exists in the context of the function definition (though sometimes we may want to name our variables differently anyways to avoid confusion)
# 3. "return" exits the function, and optionally returns one or more outputs separated by commas. In this case, we are returning the value stored in the "result" variable on line 7
# 4. We can use the result of a "return" statement by creating a variable and assigning it to a call to the function (an example of calling the function with two numbers is on line 9)
# 5. "num1" and "num2" are also sort of "placeholder" values that indicate that when the function is called, it should take two arguments that should *probably* be numbers
# 6. Python does not enforce what type of variable we pass to the function, and hence, line 12 would result in an error (our function would try to add a string to a number and error out)

# Problem 1: Fahrenheit to Celcius converter
def convert_to_celcius(temp_f):
  temp_c = (temp_f - 32) * (5/9)
  return temp_c

print(convert_to_celcius(95)) # => 45

# Both examples below will result in "Found it!" being printed (note that strings get converted to a sequence of characters by Python underneath the hood to make the second example possible)
if 'apple' in ['apple', 'orange', 'pear']:
  print('Found it!')
  
if 'a' in 'abc':
  print('Found it!')
  
# Problem 2: Given a list of movies, print "<movie_name> is an A-mazing movie!" if it has an "a", or "<movie_name> is kind of boring" otherwise
movies_list = ['Harry Potter', 'Sherlock Holmes', 'A Quiet Place']

for movie in movies_list:
  if 'a' in movie:
    print('{} is an A-mazing movie!'.format(movie))
  else:
    print('{} is kind of boring'.format(movie))
