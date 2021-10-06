# Example values
sequence = [1, 2, 7, 10, 15, 99]
target_value = 99

def binary_search (sequence, target_value):
    # midpoint = 2
    # sequence[midpoint] = 7

    # If the value at midpoint does not equal the target value, then we have the wrong position

    # First iteration: sequence = [1, 2, 7, 10, 15, 99]
    # Midpoint = 2
    # Second iteration: sequence = [10, 15, 99]
    # Midpoint = 1

    offset = 0 # offset = number of times we've shifted backward because of getting rid of some of the data
    #This prevents offset from being reset every time we run the loop
    while True:
        midpoint = (len(sequence) - 1) // 2
        if sequence[midpoint] != target_value:
            if target_value < sequence[midpoint]:
                sequence = sequence[0:midpoint]
            elif target_value > sequence[midpoint]:
                length_of_sequence = len(sequence)
                sequence = sequence[midpoint+1:] 
                offset = offset + length_of_sequence - len(sequence)
        else:
            return midpoint
        if len(sequence) == 1:
            break

print(binary_search(sequence, target_value))

# Example: target value is 99
# [1, 2, 7, 10, 15, 99] -> offset = 0
# [10, 15, 99]          -> offset = 3
# [99]                  -> offset = 5

# Example: target value is 2
# [1, 2, 7, 10, 15, 99] -> offset = 0
# [1, 2] -> offset = 0
# [2] -> offset = 1

# TODO: Still won't work if target_values are always less than the midpoint !!
