# A function s a reusable block of code that  perform a specific task.
# Functions do not perform any action or "function" until they are called.
# WIthout finctions , you'd repeat code everywhere- define it once , call it whenever needed.
# Functios always return a value
# "def" defines functions

# def <name of function>:
#     function body (must be 1 to ~ number of lines)

print("\nHello, I'm above the function")

def test():
    print("\nHello, I'm inside the function")
    print("This is another line inside the function!")

# CALL/EXECUTE THE FUNCTION
test()

print("\nHello, I'm below the function")


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