age = 30

# Below two statements have the same result
print(f"I am {age} years old")
print("I am {} years old".format(age))

# A benefit of using .format() is that you can delay formatting the string
some_str = "I am {} years old"
some_str.format(100)

random_word = "My favorite word is {}"
#I can write other code and do this later
random_word.format("burgundy")
#We didn't print this yet

print("My cat Hagrid is {}, my cat Aobai is {} and my cat Huabi is {}".format("silver", "white silver", "gray and cream"))

favorite_fruit = "Pears"
print(f"My favorite fruit is {favorite_fruit}.")

square_feet = 450
if square_feet <= 600:
	print("That's my apartment in San Francisco")
else:
	print("That's my apartment in Chicago")
    
while square_feet in range (400, 500):
	print("Welcome to Rose's apartment in San Francisco!")
#This while just keep printing. It would make more sense if this were something that would become false at some point.

i = 5
while i in range (5, 10):
	print(i + 2)
    i = i + 1
#10 is not included so 11 (9 + 2) will be the last thing to print
#while loops are great when you don't know how many times the loop will run, so the above should actually be a for loop

# This will loop until i == 7, then exit
while True:
	print(i + 2)
    i = i + 1
    if i == 7:
    	break

# The best practice way to use a for loop to print every number from 5 through 0 (plus 2)
for j in range(5, 10):
  print(j + 2)
  
  
# Practice problem: print a multiplication table for the number 5 (from 1 to 10)
# Example output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50

# All three for loops below accomplish the same goal
for x in range (1, 11):
	print("5 * " + str(x) + "=" + str(x * 5))
    
for x in range (1, 11):
	print("5 * {} = {}".format(x, 5 * x))

for x in range (1, 11):
	print(f"5 * {x} = {5 * x}")
    
   
# Practice problem: Given a list: [1,2,3,4,5], print every number EXCEPT 3

# Both for loops below accomplish the same goal
for k in range (1, 5):
  	if k == 3:
    	continue
   	print(k)
    
for k in range (1, 5):
  if k != 3:
    print(k)
   
# Boolean Operators in Python:
# AND: "and"
# OR: "or"
# NOT EQUAL: "!="
# NOT: "not"

favorite_fruit = input("Your favorite fruit: ")
if favorite_fruit == "Blackberries" or favorite_fruit ==  "blackberries":
	print("Let's make blackberry pie!")
else:
    print("What do you want to make?")

