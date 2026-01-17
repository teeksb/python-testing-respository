# Step 1: OPeneing and Reading a file
file = open("Sample - Superstore.csv", "r")
content = file.read()
file.close()

# print(content)

# Absolute file path - gives the full, exact location of a file starting from the root of the computer.
# Always points to the exact file, No ambiguity.
# e.g C:\Users\Alex\Documents\python_training\Week4_Dictionaries2\Day3_CSV\intro.py
# 
# Relative file path - A relative path describes the file location relative to the current working
#  directory (where the script is run).


# Step 2: Reading line by line (Row by Row)
file_ = open("Sample - Superstore.csv", "r")

# Read first line header
header = file_.readline()


# Read other lines
for line in file_:
    print(line.spilt(","))
    print("="*20)

print(header)

file_.close