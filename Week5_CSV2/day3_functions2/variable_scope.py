# What is scope?
# Scope = Where Python can see your variable

# Two types of scopes:

# _Global Scope:
# Variables created using this type are set to be created at the main level, this means everyone can see them. It is
# created oyside any function, class etc.

customer_name = "Alice"
def greet():
    print(f"Hello, {customer_name}")

greet() #WOrks! Prints: Hello , Alice
print(customer_name) #Works! Prints: Alice


# Local Scope 
# Variables created isnide a function - only within the functon can it be used.

def calculate_tax():
    tax_rate = 0.08  #This variabke only exists inside the function
    return tax_rate * 100

print(calculate_tax())  # Works! Prints 8.0

try:
    print(tax_rate) # ERROR! Can't see tax_rate outside the "calculate_tax() function" becasue it was definded inside the functi
except:
    print("Can't see tax_rate outside the 'calculate_tx' function")



# READING GLOBAL VARIABLES - Works fine
print("*****************************************************")

discount_rate = 0.10

def calculate_discount (price):
    discount = price * discount_rate
    return discount
print(calculate_discount(800))


print("*****************************************************")

# Reassigning Global Variables
def calculate_total_a(price):
    discount_rate = 0.13 #reasssigning the variable to a new value.
    discount = price * discount_rate

    #Here the value of "discount_rate" has been temporaily re-assigned (within the function)
    # However, the initial value of the variable remains the same outside of the function.
    print("What is discount rate?", discount_rate)

    return price - discount


print("*****************************************************")

# Modifying Global Variables
def calculate_total_b(price):
    #ERROR! (You can't modify global variables in this manner (within a function)
    discount_rate = discount_rate + 0.3
    discount = price * discount_rate

    return price - discount

calculate_total_b(800)


# Modifying Global Variables(2)
def calculate_total_b(price):
    #Here it works because its referencing the global discount_rate
    # Any chnage/modification made to the value of the variable at this point will be reflected at the global scope
    global discount_rate

    discount_rate = discount_rate + 0.3

    discount = price * discount_rate

    return price - discount

calculate_total_b(800)
# print(calculate_total_b(800))
print("What is discount rate?", discount_rate)

