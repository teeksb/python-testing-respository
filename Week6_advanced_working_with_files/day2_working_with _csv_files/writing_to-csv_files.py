import csv

# Sample data 
data = [
    # ["Name", "Score", "Grade"]
    ["Alice", 93, "A"],
    ["Bob", 85, "B"],
    ["Mike", 73, "C"],
    ["Harrison", 97, "A"],
    ["Bob", 61, "D"],
]

# Assuming the headers were not defined

headers = ["Name", "Score", "Grade"]
data = [headers] + data
print(data)


# Write to a CSV file
with open ("files/students_grades.csv", "w", newline = "") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)

print("Done writing to 'student_grades.csv'")

