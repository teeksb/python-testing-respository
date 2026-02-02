import os
from pprint import pprint

# File and directory operations
# Process management
# Environment variables
# Path manipulation

# Returns absolute path
cwd = os.getcwd()
print("\nMy current working directory is:")
print(cwd)
print("")

cwd_content = os.listdir()
print(cwd_content)
print("")

cwd_content.sort()
pprint(cwd_content)
print("")

if os.path.exists("C:\\Users\\Jubril\\Documents\Python_Training\Week5_CSV2\\day1_working_with_files\\Files\\example.txt"):
    print("example.txt found!")
else:
    print("Cannot find example.txt!")

# if os.path.exists("Sample Directory"):
#     # Navigate into the directory and create a new file
#     pass
# else:
#     # create the folder first
#     pass

if os.path.exists("Sample Path") is False:
    # Boolean expression abov has to resolve to True before the code in the if block runs
    os.mkdir("Sample Path")

print("")

# Create directory with try/except block
# try/except - if something inside try fails python jumps to except and the program continues.
# try:
#     risky_code
# except:
#     fallback_logic

try:
    os.mkdir("Sample Path")
    print("Sample Path directory created!")
except FileExistsError:
    print("AN error occurred! Check to ensure the directory doesn't already exist.")


print("")
abs_path = os.path.abspath('example.txt')
print(f"Absolute path: {abs_path}")

print("")
data_file = os.path.join('data', 'students', 'grades.txt')
full_path = os.path.abspath(data_file)
print(f"Absolute path: {full_path}")