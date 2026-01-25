# get() method is used to get an item by their key
from pprint import pprint
person = {
    "first_name": "Mary",
    "last_name" : "Doe",
    "age": 50,
    "pets": {"dog" : "Frieda", "cat": "Sox"},
    "kids": ["Joe", "Martha", "Sarah"]
}

# get method- sed to retrieve a dictionary item using a key name
# Note that when using the get() methid, if the key provided does not exist
# None will ene returened. Hoever, when using the square brcket an error will be thrown"
print("First Name (with get() method):",person.get("first_name"))
print("First Name (without method):",person["first_name"])


person_b = {
    "first_name": "Amanda",
    "last_name" : "Doe",
    "age": 50,
    "pets": {"dog" : "Frieda", "cat": "Sox"},
    "kids": ["Joe", "Martha", "Sarah"]
}

print ("***************************************")

# clear method - deletes dictionary
person_b.clear()
pprint(person_b)

print("*************************")
pprint(person)

print("*************************")

# copy() - creates a shallow mirror/copy of the dictionary.
person_a = person.copy()
pprint(person_a)

print("**************************")
# Items method - returns a list conatining a tuple of each key-value pair
pprint(person.items())

print("**************************")
# Items method - returns a list of all the values in the dictionary
pprint(person.values())

print("**************************")
# Keys- returns a list of all the keys in the dictionary
pprint(person.keys())


print("**************************")
# Pop- removes the element with the specified key and returns the value
lastName = person.pop("last_name")
print("The last name is", lastName)
pprint(person)
pprint(person["last_name"])
print("\n")
