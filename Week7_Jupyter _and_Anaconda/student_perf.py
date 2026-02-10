import csv
from pprint import pprint


STUDENT_DATA_FILE = "files/students_record.csv"

file = open(STUDENT_DATA_FILE, "r")
content = file.read()
file.close()


# def load_student_data(filename):
#     """Load student data from a CSV file into a list of dictionary items"""

#     students = []
#     int_fields = [
#     "age", "grade_level",
#     "math_score", "science_score", "english_score", "history_score"
# ]

#     with open (filename, "r") as file:
#         reader = csv.DictReader(file)


#         for row in reader:
#             print(row)
#             for field in int_fields:
#                 try:
#                     row[field] = int(row[field])
#                 except ValueError:
#                      row[field] = None   # or 0 if you prefer
                
#         try:
#             row["attendance_rate"] = float(row["attendance_rate"]) * 100
#         except:
#              row["attendance_rate"] = None
#         students.append(row)
        
#     return students


# students= load_student_data(STUDENT_DATA_FILE)
# print("\n")
# pprint(students)




def make_int(value):
        try:
            return int(value)
        except ValueError:
            return None

def make_float_percent(value):
        try:
            value = float(value)

        # only convert if it's a decimal (0–1 range)
            if value <= 1:
                return value * 100
            else:
                return value

        except ValueError:
            return None
        
def load_student_data(filename):
    """Load student data from a CSV file into a list of dictionary items"""

    students = []
    int_fields = [
    "age", "grade_level",
    "math_score", "science_score", "english_score", "history_score"
]
        
    with open (filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                    for field in int_fields:
                        row[field] = make_int(row[field])

                        row["attendance_rate"] = make_float_percent(row["attendance_rate"])

            students.append(row)
    return students


students= load_student_data(STUDENT_DATA_FILE)
print("\n")
pprint(students)
