from pprint import pprint

car = dict(
    brand = "Ford",
    model = "Mustang",
    engineLitre = 5.0,
    transmission = "manual"
)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "engineLitre": 5.0,
    "transmission": "manual",
}


print("********************")
# You access values in a dictionary using a square bracket and the name of the key as a string within the brackets.
trans = car["transmission"]
print("Car transmission is:", trans)
print(car["brand"])


person = {
    "first_name": "Mary",
    "last_name" : "Doe",
    "age": 50,
    "pets": {"dog" : "Frieda", "cat": "Sox"},
    "kids": ["Joe", "Martha", "Sarah"]
}

pprint(person["kids"])
pprint(person["kids"][1])
print ("What's the nake of the 2nd child?")
secondChild = person["kids"][1]
print("Name of the 2nd child is:", secondChild)


print("\n")
print("What is the name of his dog? ")
dog_name = person["pets"]["dog"]

print("Name of dog is:", dog_name)
# print(f"The name of his dog is: \n{person["pets"]["dog"]}")


