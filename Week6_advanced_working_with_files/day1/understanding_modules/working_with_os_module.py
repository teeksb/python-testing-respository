import os
from pprint import pprint

# File and directory operations
# Process maanagement
# Environment variables
# Path manipulation

cwd = os.getcwd()

print("My current working directory is:")
print(cwd)
print("")


cwd_content = os.listdir()
print(cwd_content)
print("")

cwd_content.sort()
pprint(cwd_content)
print("")

# To know if a file exists
if os.path.exists("C:\\Users\Jubril\Documents\Python_Training\Week5_CSV2\day1_working_with_files\Files"):
    print('example.txt found!')
else:
    print("Cannot find example.txt!")


if not os.path.exists("Sample Directory"):
    os.mkdir("Sample Directory")