list_of_numbers = [1, 13, 45, 66, 68, 70, 80]
# Remember that list is its own type
target_number = 70

def binary_search(list_of_numbers, target_number):
    low_index = 0
    high_index = len(list_of_numbers) - 1 # No extra parentheses here. List is its own type and we want to subtract from the lenth of the list not the list itself. Also, the parentheses should only take the argument of the function.

    while low_index <= high_index:
        #middle_index = low_index + (high_index - low_index) // 2
        # This accomplishes the same goal as above and is a bit easier to read
        middle_index = (high_index + low_index) // 2
        if list_of_numbers[middle_index] == target_number:
            return middle_index
        elif list_of_numbers[middle_index] < target_number:
            low_index = middle_index + 1
        else: #middle must be greater than the target number
            high_index = middle_index - 1
    return -1
        
final = binary_search(list_of_numbers, target_number)

if final == -1:
    print("Your target number cannot be found in the list.")
else:
    print("{} can be found at position {}".format(target_number, final))
    
# Common Error Type Explanations
# Syntax Error: The grammar of the code is wrong (e.g. missing colon, wrong indentation, etc.)
# TypeError: We are trying to compare incompatible types of variables (e.g. adding an int to a string)
# NameError: The name of the variable does not exist 
