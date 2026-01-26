

def add(a, b): # When defining a function, the placeholder variables you place in-between the brackets are referred to as "parameters"
    print(a + b)
    tuple = (a, b)
    print(tuple)

# print(a)
# print(b)

# Variable Scope

add(20, 9) # When you call a function, the values you pass in-between the brackets are referred to as "arguments"
add(13, 48)
add(90, 14)


# A function being assigned to a variable.
addition = add

# Pass a function as an arguement to other functions
def operations(a, args):
    return a(*args)
operations (add, [12, 15])


# Return a function from another function

def _operations():
    def addition(*values):
        return sum(values)
    return addition


result = _operations()([12,15])
print(result)



def calc():
    return "Calculation"

# A function can be stored in a datat structure (like lists, dictionaries)

student = {
    "name": "Tosin Kasaba",
    "gender": "Female",
    "calculate_scores": calc,
}

student["calculate_scores"]()