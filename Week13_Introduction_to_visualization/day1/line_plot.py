import matplotlib.pyplot as plt #load plotting module

import pandas as pd


def load_students(filename: str) -> pd.DataFrame:
    df = pd.read_csv(filename)

    class_level_map = { # converts numeric class levels into readable school labels.
        10: "SS1",
        11: "SS2",
        12: "SS3",
    }

    # Convert selected columns to numeric where needed
    numeric_columns = [ # Create a list of columns to convert to numbers: these are columns  want to make sure are treated as numeric values.
        "English Language",
        "Literature in English",
    ]

    for col in numeric_columns: # loop through tose columns one at a time
        if col in df.columns: # safety check - check whether colums exists - because if it doesnt python will raise an error
            df[col] = pd.to_numeric(df[col], errors="coerce")  # convert that column into numeric values, errors= "coerce" means if the value cannot be converted, replace it with NaN

    # If score columns ending with "_score", convert them
    score_columns = [col for col in df.columns if "_score" in col] # loop through column names in df.coluns and keep only the ones that conatin "_score"
    for col in score_columns:  # loop through score columns one by one convert each column to numeric.
        df[col] = pd.to_numeric(df[col], errors="coerce") #convert each column to numeric, invalid values become Nan and valid number stay as numbers.
        df[col] = df[col].fillna(df[col].min())   #This replaces missing values (NaN) in that column with the minimum value in the same column.

    # Replace numeric class levels with labels
    if "class_level" in df.columns:  # check if class_level exists - always good to check befor trying to modify it
        df["class_level"] = df["class_level"].replace(class_level_map)  #Replace class level numbers with labels

    return df
students_df = load_students("../../data/students.csv")

ss1_math = students_df[ students_df["class_level"] == "SS1"].iloc[0:50]["Mathematics"] # 0R students_df.loc[ students_df["class_level"] == "SS1", "Mathematics"]
ss2_math = students_df[ students_df["class_level"] == "SS2"].iloc[0:50]["Mathematics"]
ss3_math = students_df[ students_df["class_level"] == "SS3"].iloc[0:50]["Mathematics"]


#Create a figure axes

fig, ax = plt.subplots(figsize=(10, 6)) 
# fig - the canvas(page), ax - the chart. fig szie (width =10,height =6) is the default size most commonly used because it produces a chart with a nice readble aspect ratio.
# It fits nicely in Jupyter notebooks
# Works well on laptop screens
# Leaves room for title and legends
# Produces readable fonts
# Small chart - figsize(6,4) - god for dashboards
# Medium chart - figsize(8,5) -
# Large presentation chart - figsize(12, 7) 
# WIde chart- figsize(14,6) - good for stock prices, production curves and time-series data

#Create a line representing the distribution of math scores

ax.plot(range(len(ss1_math)), sorted(ss1_math), label="SS1", color="blue", marker="s")
ax.plot(range(len(ss2_math)), sorted(ss2_math), label="SS2", color="green", marker="^")
ax.plot(range(len(ss3_math)), sorted(ss3_math), label="SS3", color="red", marker="o")

# Add labels and title -these are he four most common formatting commands
ax.set_title("Distribution of Mathematics Scores by Class Level")  # set chart title
ax.set_ylabel("Mathematics")  # labels vertcial axis
ax.set_xlabel("Student Rank")   # labels horizontal axis
ax.legend() #display the legend /shows line labels


#Display teverything we've created
plt.show() 