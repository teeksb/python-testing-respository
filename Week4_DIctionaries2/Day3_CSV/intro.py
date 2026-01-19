

# Step 1: Opening and Reading a File
file = open("Sample - Superstore.csv", "r") #This line opens a file called Sample - Superstore.csv
#"r" means read mode (you’re only reading the file, not changing it).Python now keeps this file open and stores it in the variable file
content = file.read()    #This reads the entire contents of the file,everything in the CSV (all rows and columns) is pulled into memory,
#the text is stored as one bring string inside "content"
file.close() # this closes the file. It's good pracrice to (always close files you open).

print(content) #prints the file's content to the screen.


#Another way to write the above tat automatically closes the file , even if something goes wrong
# with open("Sample - Superstore.csv", "r") as file:
#     content = file.read()

# print(content)



# Absolute file path: Path to the file on your laptop/deskop or cloud/online - from root to end - files can be traced down to roor
# e.g C:\Users\Jubril\Documents\Python_Training\Week4_DIctionaries2\Day3_CSV


# Relative file path: Path to the file relative to the Python file importing it.
#e.g # C:\Users\ADMIN\Source\Data Science Bootcamp\Cohort 2\Week_5_-Working_with_Files\Sample - Superstore.csv


# Which should you use?
# Use relative paths when:
# Working on projects
# Sharing code
# Using Git
# Running scripts on servers

# Use absolute paths when:
# Debugging locally
# Writing one-off scripts
# You must reference a fixed system location
# Step 2: Reading Line by Line (Row by Row)


# file_ = open("Sample - Superstore.csv", "r")

# # Read first line (header)
# header = file_.readline()
# header.split(",")

# # Read all other lines
# for line in file_:
#     print(line.split(","))
#     print("="*20)

# file_.close()


# Step 3: Using 'with' statement (Best practice)
with open("Sample - Superstore.csv", "r") as file:
    # Read header
    header = file.readline().strip()
    print("Columns:", header)

    for line in file:
        print(line.strip())
        print("="*20)