file_path = "files/example.txt"

with open(file_path, "r") as file:
    for line in file:
        print(line.strip())
    print("")
    print("="*30)
    print("")

    # Reset the line pointer back to the first line
    file.seek(0)

    content = file.read()
    for line in content.split("\n"):
        print(line)
