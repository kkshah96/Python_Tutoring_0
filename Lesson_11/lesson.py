# 'sequence' is an ORDERED list of numbers
# 'target' is the number of which we are trying to find the INDEX

def binary_search(sequence, target):
  # TODO: Is there a way we can combine this 'while' satement with the 'if' statement on line 12?
  while True:
    # 'midpoint' is the INDEX of the middle element
    midpoint = len(sequence) // 2
    
    # If we have not found the target, keep splitting sequence in half until we have
    # We can use re-assignment and list slicing to keep modifying the sequence to become smaller and smaller
    if sequence[midpoint] != target:
      if sequence[midpoint] < target:
        sequence = sequence[midpoint:]
      if sequence[midpoint] > target:
        sequence = sequence[0:midpoint]
      
      # Update the midpoint to reflect the new sequence
      midpoint = len(sequence) // 2
    else:
      # If we have found the target, return the index of the target
      return midpoint
    
    # If we are down to one element and it is NOT the target, the target does not exist in the input
    # Break to avoid infinite loop
    if len(sequence) == 1:
      break
      
      
# Example values
sequence = [1, 5, 7, 10, 15, 21]
target = 7

# The below code will result in the following, where 'i' refers to the start of the respective loop iteration
# i = 0: midpoint = 3, sequence = [1, 5, 7, 10, 15, 21] => continue loop
# i = 1: midpoint = 1, sequence = [1, 5, 7] => continue loop
# i = 2: midpoint = 0, sequence = [7] => return midpoint

# TODO: Does this function call return the right number?
result = binary_search(sequence, target)
  
  
