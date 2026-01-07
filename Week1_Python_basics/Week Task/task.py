#Mathematics Test Score

print("Grade 1 Test Result 2025")
print()

student_1 = input("What is your name? ")
student_1_score = int(input("What is your score? "))


student_2 = input("What is your name? ")
student_2_score = int(input("What is your score? "))


student_3 = input("What is your name? ")
student_3_score = int(input("What is your score? "))


print()
print()
print("*************")
print("Cumulative Result")
result_1 = f"{student_1}'s score is = {student_1_score}"
result_2 = f"{student_2}'s score is = {student_2_score}"
result_3 = f"{student_3}'s score is = {student_3_score}"

print(result_1)
print(result_2)
print(result_3)


print()

class_average = int((student_1_score + student_2_score + student_3_score ) /3)
percentage_class_average = int((student_1_score + student_2_score + student_3_score) /3) * 100
print("Class Average is ", class_average)
print(f"Percentage Class Average is {class_average}%")


