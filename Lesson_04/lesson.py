city = "Nagasaki"

print(city[:4])
print(city[0:4])

print(city[::-1])

print(city[5::1])

# Prints "ika"
print(city[:-4:-1])
print(city[-1:4:-1])
print(city[::-1][:3]) # This one is the most intuitive (reverse the string, then go up until the 3rd character)

# When we use a negative start or end, the start becomes uninclusive, and the end becomes inclusive
print(city[-3:-2:1])  # -> 'a'

num = 5
if num >= 0:
    if num == 0:
        print("Zero")
    if num > 0:
        print("Positive number")
elif num < 0:  # else: (will produce same result and is preferred)
    print("Negative number")

# The cleanest way to do the above flow:
# Hint: We could organize these if statements in any order, but there is no need for nested if statements here as
# we can achieve the same result with one if/elif/else statement
if num == 0:
    print('Zero')
elif num > 0:
    print('Positive Number')
else:
    print('Negative umber')

# Let's say usernames are Sarah, Katie, Alex and Josh
# The below will print "Welcome to Level 1"
username = "Josh"
if username == "Josh" or username == "Alex":
    print("Welcome to Level 1")
elif username == "Sarah" or username == "Katie":
    print("Welcome to Level 5")

# The below will print "Josh"
if username == "Josh":
    print(username)
elif username == "Alex":
    print(username)