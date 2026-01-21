# Relative path

from pathlib import Path #Import the Path class from Python's pathlib so I can work with file and folder paths easily.

base = Path(__file__).parent  #".parent" the directory containing teh script while ""_file_" is the pathof the Python script itself"
file_path = base / "example.txt" # "example.txt" a file relative to that directory
# This states  find "example.txt" realtive to where thiscript lives.

with open(file_path, "r") as file:
    for line in file:
        print(line)

    # print("")

    # Reset the line pointer back to the first line
    # file.seek(0)

    # content = file.read()
    # for line in content.split("\n"):
    #     print(line)



