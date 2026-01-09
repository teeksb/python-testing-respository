# get() method is used to get an item by their key
from pprint import pprint
person = {
    "first_name": "Mary",
    "last_name" : "Doe",
    "age": 50,
    "pets": {"dog" : "Frieda", "cat": "Sox"},
    "kids": ["Joe", "Martha", "Sarah"]
}

# get method- sed to retrieve a dictionary method using a key name
print("First Name (with get() method):",person.get("first_name"))
print("First Name (without method):",person["first_name"])


person_b = {
    "first_name": "Amanda",
    "last_name" : "Doe",
    "age": 50,
    "pets": {"dog" : "Frieda", "cat": "Sox"},
    "kids": ["Joe", "Martha", "Sarah"]
}


# clear method -deletes dictionary conetnbt
person_b.clear()
pprint(person_b)