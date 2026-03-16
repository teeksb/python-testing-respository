from utils.students_record_utils import load_student_records

students_df = load_student_records("../data/students.csv")

class_groups = students_df.groupby("class_level")

print("\n")

# Count of student in each class level
print("Number of students per class level:")
print(class_groups.size())

print("\n")

custom_agg = {
    "attendance": ["min", "max", "mean"],
    "Mathematics": ["mean", "median", "std"],
    "English Language": ["mean", "median", "std"],
}

class_analysis = class_groups.agg(custom_agg)

print("\nCustom aggregation by class level:")
print(class_analysis)
print("\n")