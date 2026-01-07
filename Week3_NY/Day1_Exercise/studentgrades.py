# A simple program that helps teachers to calculate students grades.
# Ask the teacher for the number of students 
# For each student ask for the student's name and aso ask for their test score.
# Check if score is valid between 0 and 100
# Calculate average of all scores.
# Tell the teacher : who failed (score < 50) , who passed (score >=60)
# Calculate the class average
# The highest and lowest scores.


print ("")
print ("")
print ("====================================================")
print (""" 
Student Grades Tracker Project
Author: Tosin Kasaba
Description: A program hat tracks student grads, calculates class vaerage, and identifies who passed or failed
       """)
print ("=================================================")
print("")


# STep 1: Ask how many students
num_students = int(input("How many students do you want to grade? "))

# Initialize all neccessary variables for calculations
total_score = 0
passed_students = []
failed_students =[]


for num in range (num_students):
    print(f"\n--- Student {num + 1} ---")

    # First time loop , get the student name
    student_name = input("Enter student name: ")

    # Get and validate test score
    student_score = float(input( f"Enter score for {student_name}: "))

    while student_score < 0 or student_score > 100:
        print ("Invalid score! Please enter a score between 0 and 100")
        student_score = float(input(f"Enter score for {student_name}: "))
    
    print("Score recorded!")

    # Add to the total for calculation of average
    total_score = total_score + student_score
    print("The total score is ", total_score)

    # Check if the student passed or failed
    if student_score >= 60:
        passed_students.append((student_name, student_score))
    else:
        failed_students.append((student_name, student_score))

# names = [] list- mutable
# names = ("CHris", "Dan", "Sarah") tuple - immuatble

class_average = total_score / num_students

print("\n " + "=" * 50)
print ("GRADE REPORT")
print("=" * 50)

print ("\nSTUDENTS WHO PASSED:")
for student in passed_students:
    print(f"   - {student[0]}: {student[1]}")
else:
    print("0 (No student passed)")


print ("\nSTUDENTS WHO FAILED:")
for student in failed_students:
    print(f"   - {student[0]}: {student[1]}")
else:
    print("0 (No student failed)")

print(f"\nCLASS AVERAGE is: {class_average}")
