print(int(5.5))
print(float(2))
print(input("tell me your name"))
temperature = 70
if temperature >= 70:
    print("go outside")
elif temperature > 50:
    print("maybe go outisde?")
else:
    print("be lazy and stay inside")

print("this\thas a tab")
print("this\nwill be on more than one line")
print(r"this is a raw string and the backslash\ character will be ignored")
print("this is another way to escape the backslash character: \\")
print(10 % 3)

# Outputs: 100
print(10 ** 2)

# Outputs: 1000
print(10 ** 3)

# Outputs: 2
print(4 ** 0.5)

# JavaScript Syntax:
"""
function createanalienpet(age, fur_color)
{
    console.log("age: " + age, "fur color: " + fur_color)
}

createanalienpet(4, pink)
"""

# Python Syntax:
def createanalienpet(age, fur_color):
    print("age: " + age + "fur color: " + fur_color)

createanalienpet(4, "pink")

# Instead of having the function print, have it return a list containing the attributes (later we will look at
# creating our own AlienPet object and returning that instead)
def createanalienpet(age, fur_color):
    return [age, fur_color]

age_fur_color_list = createanalienpet(6, "purple")
print(age_fur_color_list)

# Can chain operations (this will output the same product as lines 48 and 49 combined)
print(createanalienpet(6, "purple"))

# List is just a sequence of data points
list1 = [1, 2, 3, 4]


# Objects in *most* programming languages are structures that have properties and functions
# Classes are blueprints for objects

# Dog class (blueprint for Dog)
# JavaScript Syntax:
"""
class Dog {
    constructor(age, breed) {
        this.age = age;
        this.breed = breed;
    }
}

const cody = new Dog(6, "golden retriever")
const henry = new Dog(7, "daschund")
"""

# This is called an object in Javascript, but in Python this is known as a "dict" or Dictionary
# JavaScript Syntax:
"""
cody = {
    age: 6,
    breed: "golden retriever",
    homeLocation: {
        city: "new york",
        street: "monroe"
    }
}
"""

# Curly brackets to specify a dictionary in Python
# Python Syntax:
cody = {
    "age": 6,
    "breed": "golden retriever",
    "homeLocation": {
        "city": "new york",
        "street": "monroe"
    }
}




