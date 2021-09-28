# 'sequence' is an ORDERED list of numbers
# 'target' is the number of which we are trying to find the INDEX

# Example values
sequence = [1, 5, 7, 10, 15, 21]
target = 7

def binary_search(sequence, target):
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
    else:
      # If we have found the target, return the index of the target
      return midpoint
    
    # If we are down to one element and it is NOT the target, the target does not exist in the input
    # Break to avoid infinite loop
    if len(sequence) == 1:
      break
      
    
  
  
