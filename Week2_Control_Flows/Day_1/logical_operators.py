# Logical operators are used to oombine/modify comaprison operations. 
# Logical operators connect comparisons e.g Is age > 18 and has ID?
# They combine or modify Boolean values (True / False).
# They help python answer bigger questions made up of smaller yes/no questions.
# Conditions are checked top to bottom
# Only one block executes
# else must come last but its optional
# # elif is optional (you can have many or none)
# Start with the most specific condition, end with the most general.
# Logical operators - Connect answers

# The three logical operators:
# and - both must be True   - ALL conditions
# or   -  at least one True  - ANY condition
# not  -  reverse result     - OPPOSITE

# and needs all True

# or needs any True

# not flips the result

# Operator precedence matters: python evaluates in this order : not - and - or

# They do NOT:

# Compare values (that’s comparison operators like ==, >)
# Do math

# They answer questions like:

# “Are both of these true?”

# “Is at least one true?”

# “Is this not true?”

# One-line rule to remember 
# With and, the first falsy value wins.
# If none are falsy, the last truthy value wins.

# Another rule:
# and -first fasly wins
# or - first truthy wins

# and Operator (ALL must be True)
age = 35
age > 18 and age < 65 #both true, True and False  - # False
True and False   # False

# or Operator (ANY can be True)
age = 70
age < 18 and age > 65 # true (second condition is true), False or True -   # True


# not Operator (ANY can be True)
logged_in = False

not logged_in   # True
# not True - False , not False - True


age = 17
has_id = True


# "and" operator - here all sides must be true
# all conditions must be true

if age >= 18 and has_id:
    print("Give access")
else:
    print("No access")



# "or" operator- onnly one side of the statement can be true for it resolve as true
# atleast one consition must be true

if age >= 18 or has_id:
    print("Give access")
else:
    print("No access")


# "not" operator - it reverses a condition /it negates the result of an operation.
logged_in = False

if not logged_in:
    print("You are a guest")
else:
    print("welcome back")




# "and" operator - all conditons must be true
age = 17
had_id = True

if age >= 18 and had_id == True:
    print("Give access")
else:
    print("No access!")

# "or" operator - only one sude can be true for it to resolve as true -atleast ine condition must be true
if age >=18 or had_id == True:
    print("Give access")
else:
    print("No access")


# "not" operator -it gives the reverse of a condition - it negates the  result of an operation
print(not (5==5))
print(5==5)
print (not(False))
print (not(True))


logged_in = True
if not logged_in:
    print("You're a guest")
else:
    print("Welcome back")


#Discount eligibility

age = 65
is_student = False

if age >= 60 or is_student:
    print("Discount applied")
else:
    print("Sorry, no discount for you!")