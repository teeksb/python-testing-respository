print("GRADE 1 MATHS ASSESSMENT SYSTEM")
print("*****************************************")
print("*****************************************")
print("")
print("Welcome Mr Chris")
print("")
number_of_students = int(input("How many Grade 1 Maths students will you enter scores for today?: "))

total_score = 0
passed = 0
failed = 0
highest_score = 0
lowest_score = 100



for i in range(number_of_students):
    print(f"\n Student {i + 1}")
    name = input("Enter name of student: ")

    score = int(input("Enter student's test score: "))
    while score < 0 or score > 100:
        print("Invalid score. Score must be between 0 and 100.")
        score = int(input("Enter student's test score: "))

    total_score = total_score + score #determine total score after the inputs/looping

    if score >= 60:   
        passed = passed + 1
        # print(name, "PASSED")
    else:
        failed = failed + 1
        # print(name, "FAILED")

    # highest score
    if score > highest_score:
        highest_score = score

    # lowest score
    if score < lowest_score:
        lowest_score = score

# class average
class_average = round(total_score/number_of_students)


print("\n********** CLASS SUMMARY **********")
print("Number of students:", number_of_students)
print("Class average:", class_average)
print("Students passed:", passed)
print("Students failed:", failed)
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)

