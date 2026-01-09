from pprint import pprint

library = {
    "The Hobbit": {
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "genre": "Fantasy",
        "read": True,
    },
    "Dune": {
        "author": "French Herbert",
        "year": 1965,
        "genre": "Fiction",
        "read": False,
    },
}

# pprint(library.items())

for item in library.items():
    print("Book Title", item[0])
    print("Book Details", item[1])
    print("\n")

print("\n")
print("***********************************************************************************")
# spreading method
for (bookTitle, bookDetails) in library.items():
    print("Book Title:", item[0])
    print("Book Details:", item[1])
    print("\n")