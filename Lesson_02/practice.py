# Output some text onto the console, and then read input into "name" variable
name = input("enter your name")
print(name)

# Alternatively we can achieve the same result like such, eliminating the need for the name variable:
print(input("enter your name"))

print("\"cat\tdog\that\tcoat")
print("""this can go across multiple 
lines if I keep typing""")

total = 1 + 2
print(total)

print(1 + 2)

# The built-in type function in Python will tell us the type of a data object (in this case, "float")
print(type(1.23))