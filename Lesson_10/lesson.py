low = 1
high = 1000
print("Please think of a number between {} and {}".format(low, high))
input("Press input to start")

num_guesses = 1

while True:
  guess = low + (high - low)//2
  high_low = input("My guess is {}. Should I guess higher or lower? Please" \
				   "enter \"h\" for higher, \"l\" for lower or \"c\" for correct".format(guess)).casefold()
  
  # Another way to format this code
  #
  #  high_low = input(
  #    "My guess is {}. Should I guess higher or lower? Please" \
  #	   "enter \"h\" for higher, \"l\" for lower or \"c\" for correct".format(guess)
  #  ).casefold() 
  
  if high_low == "h":
    #Guess was too low. New low end = guess + 1
    low = guess + 1
  elif high_low == "l":
    #Guess was too high. New high end = guess - 1.
    high = guess - 1
  elif high_low == "c":
    print("I guessed correctly in {} guesses".format(num_guesses))
    break
  else:
    print("Please enter \"h\", \"l\" or \"c\".")
  
  # Alternatively: num_guesses += 1
  num_guesses = num_guesses + 1
          
# Note: We started implementing binary search but this is WORK IN PROGRESS
def binary_search(low_end, high_end, target_value)
  #if this were to run only once, we could just do high_end // 2
  midpoint = low_end + (high_end - low_end) // 2
  if midpoint != target_value:
     pass # To be continued
    
      
 
