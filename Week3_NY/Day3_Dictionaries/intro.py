# A dictionary is a data type used to store data values in a key value pair.
# Values in a dictionary can be of any datat type.
# Keys must be strings.
# A dictionary is an ordered collection(as from Version 3.17) which is changeable/mutable and ordered.
# It doesn't allow duplicates
# Keys must be unique

# # Use LIST when data changes
# Use TUPLE when data is fixed
# Use DICT when data needs labels

# examples: 
# List → shopping list (you can add/remove items) - changing data

# Tuple → GPS coordinates (fixed) - fixed data
 
# Dictionary → contact card (field → value) - labeled data


from pprint import pprint


student_a = {
    "first_name": "Tosin",
    "last_name" : "Kasaba",
    "age" : 20,
    "height" : 1.65,
    "gender" : "Male",
    "registered": True,
    "skills": []
}

recent_orders = {
    "orderID": 2345666,
    "orderDate": 4554,
    "shipMode": 4554,
    "customerName": 4556,
}

pprint(student_a)
print(student_a["first_name"])


print("*************************")
# Create dictionary using dict() constructor
student_b = dict(
    first_name = "Tosin",
    last_name = "Kasaba",
    age = 20,
    height = 20,
    gender = "Male",
)

pprint(student_b)
print(student_b["first_name"])