splitString = "This string has been \nsplit over\nseveral\nlines"
print(splitString)

tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

print("""The pet shop owner said "No, no," \
'e's uh,...he's resting". """)

# Note: If we remove the backslashes here python will actually print these statements on different lines (only applies
# to triple quote strings AKA docstrings!!)
anotherString = """This string has been \
split over \
several \
lines"""

print(anotherString)

print("C:\\Users\\timbuchalka\\notes.txt")

# "r" here stands for "raw" and prints literal backslashes instead of interpreting them as escape characters
print(r"C:\Users\timbuchalka\notes.txt")
