import random

highest = 10
answer = random.randint(1, highest)
print(answer)  # REMOVE after testing
guess = 0  # initialize to any number that does not equal the answer

# While loops and if statements operate on "conditions". Conditions always evaluate to a boolean value (True or False)
# E.g. The condition "guess != answer" evaluates to True
while guess != answer:
    print("Guess any number between 1 and 10: ")
    guess = int(input())
    if guess != 0:
        pass
    else:
        break

    if guess == answer:
        print("You guessed correctly")
        break # This is not needed because the condition will become false and the loop will exit
    elif guess < answer:
        print("Guess higher")
    elif guess > answer:
        print("Guess lower")

# Instead of writing funky extra code to create an initial guess value of 0 and loop until guess != answer,
# we can just create an infinite loop using "while True", and break when the answer is found
highest = 10
answer = random.randint(1, highest)

while True:
    guess = int(input())
    if guess == 0:
        break
    if guess == answer:
        print("You guessed correctly")
        break # This is now needed, otherwise we will enter an infinite loop
    elif guess < answer:
        print("Guess higher")
    elif guess > answer:
        print("Guess lower")

# Instead of using "elif", we can write the same code with just regular if statements since we know each condition
# is mutually exclusive

highest = 10
answer = random.randint(1, highest)
while True:
    guess = int(input())
    if guess == 0:
        break
    if guess == answer:
        print("You guessed correctly")
        break # This is now needed, otherwise we will enter an infinite loop
    if guess < answer:
        print("Guess higher")
    if guess > answer:
        print("Guess lower")

# This textbook answer is also valid, but I would argue there is no need to create a nested if statement
highest = 10
answer = random.randint(1, highest)

while True:
    guess = int(input())
    if guess == 0:
        break
    if guess == answer:
        print("You guessed correctly")
        break  # This is now needed, otherwise we will enter an infinite loop
    else:
        if guess < answer:
            print("Guess higher")
        if guess > answer:
            print("Guess lower")

shopping = ["apples", "pears", "salami", "bread"]
for item in shopping:
    if item == "salami":
        continue
    print("buy " + item)

    # other ways to write this print statement:
    print(f"buy {item}")
    print("buy {}".format(item))
    print("buy", item)  # you might not be able to use this if you wanted to display it some other way instead of using the print function

# A more concise way to do the above without needing a "continue"
for item in shopping:
    if item != "salami":
        print("buy " + item)

shopping_list = ["apples", "milk", "lettuce", "cucumber", "chips"]
item_to_find = "lettuce"

# range(len(shopping_list)) => [0,1,2,3,4]
# index => 0, index => 1, ...
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

# NOTE: If we don't use break, this will run five times, for each item in the list
# However, the code will still run as expected (just become a little less efficient)

print("Item found at {}".format(found_at))

# tuples are essentially lists, but they cannot be modified
# E.g. my_tuple = ('apples', 'milk', 'lettuce')
# enumerate(shopping_list) => [(0, "apples"), (1, "milk"), (2, "lettuce"), ...]
# Note that the for loop can "unpack" tuples, and so we can access both "index" and "value" in each iteration
for index, value in enumerate(shopping_list):
    if value == item_to_find:
        found_at = index
        break

# The easiest way to solve the above problem using Python functions:
# list.index() function returns index of item
shopping_list.index("lettuce")  # => 2
print(shopping_list.index("lettuce"))
