import pandas as pd
from utils.students_record_utils import load_student_records

students_df = load_student_records("../data/students.csv")

students_df.rename(
    columns={
        "Further Mathematics": "further_mathematics",
        "Civic Education": "civic_education",
        "Computer Science": "computer_science",
        "English Language": "english_language",
        "Literature in English": "literature_in_english",
    },
    inplace=True, # means to modify the original DataFrame directly instead of returning a new one without adding this, the rename function returns a new DataFrame
)

print(students_df[["student_id", "further_mathematics", "civic_education", "computer_science", "english_language"]])



