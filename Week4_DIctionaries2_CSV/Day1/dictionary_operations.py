# Adding new entereis in a dictinary

from pprint import pprint

person = {
    "first_name": "Mary",
    "last_name" : "Doe",
    "age": 50,
    "pets": {"dog" : "Frieda", "cat": "Sox"},
    "kids": ["Joe", "Martha", "Sarah"]
}

if "gender" in person:
    print("Found the key: first_name")
else:
    print("Could not find the key")

print("****************")
person["middle_name"] = "Dummy"

pprint(person)