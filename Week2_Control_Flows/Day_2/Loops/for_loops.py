# A for loop repeats code a sepcific number of times - it is not based on a condition.
#A for loop ends on its own - it doesnt need a flag. It woulld start and end on its own.

# They are mostly used with "list" - a data type that conatains a list of items.
#Iterate - go over again

# A for loop iterates through all the items in a list - so a list will typically have a length (already) which is why a for
# loop has no flag.

# Iterable - something you can iterate iver and a "list" is an iterable as well as a "string"
# e.g 
# Basic Syntax:
# for item in collection:
#     do_something

# for iterates over a sequence (list, range, string, etc.).- for each item in this collection

# When to use for:
# Looping over lists, dicts, strings
# Known number of iterations
# Data processing
# Aggregations (sum, filter, count)
name = "Tosin Kasaba"


for char in name: #for every character in the variable/name : "Tosin Kasaba"
    print(char)

print ()
for number in range (1, 6): # range - allows you to generate an iterable object e.g a range of numbers
    print(number)

print(iter(range(50)))

for i in range(5):
    print(i)


print('/n')
for num in range(6):
    print(num)

print('/n')
names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(name)

print("")
for letter in "Python":
    print(letter)

# range(5)        # 0 → 4
# range(1, 5)     # 1 → 4
# range(1, 10, 2) # 1, 3, 5, 7, 9