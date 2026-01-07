#A list is a conatiner that holds multiple value in a single variable. Think of it like:
# A list is a data type. Just like string, boolean, integer, and float.
# A playlist with multiple songs

#List are mutable - their value can be changed after they've been created... they can be modified/changed.

# Test scores
scores = [85,92,78,95,88]

#Shopping List
shopping = ["rice", "milk", "bread", "eggs", "butter"]

# It's possible  for list to hold values if mixed data types. Although it isn't recommended.
mixed =["John", 25, False, 3.14, ["Christ", 35]]

# Its okay to define an empty list. Items can always be added later.
empty_list = []

#Common Index Error : list index out of range
#eg.
# print(mixed[9])

# It uses colon inside square bracket
# my_list[start:stop:step] start: where to begin, stop: where to stop, step: how many steps to jump each time.

nums = [0, 1, 2, 3, 4, 5]
nums[1:4]    
# Start at index 1, stop before index 4 (index 4 is not included)
# Imprtant rule to remmeber the stop index is never included

# Omitting start or stop
print ("Omitting start or stop")
print ("From the beginning")
nums[:3]
# This will give [o,1,2]

print(".......")
print ("To the end")
nums[3:]
# This will give [3,4,5]

print(".......")
print ("Entire List")
nums[:]
# This will give [0,1,2,3,4,5]

print(".......")
print ("Using step the thrid value")
nums[::2]
# Everyy second element
# This will give [0,2,4]

print(".......")
print ("From index 1, 2 every steps")
nums[1::2]
# This will give [1,3,5]


# Negative indexes (-1 will be = 5), (-2 will be 4) (-3 will be 3)
print ("Last 3 elements")
nums[-3:]
# This will give [3,4,5]

print ("Everything excep las element")
nums[:-1]
# This will give [0,1,2,3,4]

# Reverse entire list
print ("Explanantion: Start: beginning, Stop: end, Stop(-1)-move backwards")
nums[::-1]
# This will give [5,4,3,2,1,0]



# Slicing Strings works the same way
text = "Python"
print ("Fist 3 characters")
text[:3]
# This will give ["Pyt"]

print("********************")
print ("Reverse string")
text[::-1]
# This will give ["nohtyP"]

print ("Other examples")
# Remove first and last item:
# items[1:-1]

# Get top 5 results:  results[:5]
# Skip data row: data[1:]
# Copy a list safely: copy = original[:]

# Rule: slicing where start == stop gives an empty list.
# nums[2:2].... correct answer is []