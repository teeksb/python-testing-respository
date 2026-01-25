# What is a CSV - COmma-Seperated Values
# First line is usually - header
# Every line after - datat row
# Everything is read as strings

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
# full address from the root of the system
# e.g C:\Users\Jubril\Documents\Python_Training\Week4_DIctionaries2\Day3_CSV


# Relative file path: Path to the file relative to the Python file importing it. - address relative to where the script runs
# Relative paths are more portable because they don’t depend on a specific machine’s directory structure and work across environments.
#e.g Week4_DIctionaries2\Day3_CSV



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
# header = file_.readline().strip()
# header.strip().split(",")

# # Read all other lines
# for line in file_:
#     print(line.strip().split(","))
#     print("="*20)

# file_.close()


# Step 2: Using 'with' statement (Best practice)
# with open() automatically closes the file, even if an error occurs, making file handling safer and less error-prone.
# Reading files line by line reduces memory usage and prevents large or unexpected files from crashing data pipelines or slowing systems at scale.
with open("Sample - Superstore.csv", "r") as file:
    # Read header
    header = file.readline().strip() #file.readline() reads one full line from the file and moves the file pointer to the next line.
    print("Columns:", header)

    for line in file:
        print(line.strip().split(","))
        print("="*20)