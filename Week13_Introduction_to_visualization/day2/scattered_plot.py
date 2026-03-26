#Shows relationship between 2 numerical values
# They are used to visualize correlations between 2 values.

import matplotlib.pyplot as plt


import pandas as pd

def load_students(filename: str) -> pd.DataFrame:
    df = pd.read_csv(filename)

    class_level_map = {
        10: "SS1",
        11: "SS2",
        12: "SS3",
    }

    numeric_columns = [
        "English Language",
        "Literature in English",
    ]

    for col in numeric_columns:
        if col in df.columns: 
            df[col] = pd.to_numeric(df[col], errors="coerce")  
    score_columns = [col for col in df.columns if "_score" in col] 
    for col in score_columns: 
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].min())  
    if "class_level" in df.columns:  
        df["class_level"] = df["class_level"].replace(class_level_map) 

    return df
students_df = load_students("../../data/students.csv")


#Creatte the figure and axes
fig, ax = plt.subplots(figsize=(10,6))

#Cretate a scatter plot of Mathematics vs English Language scores
ax.scatter(
    students_df[students_df["class_level"] == "SS1"].iloc[0:100]["Mathematics"],
    students_df[students_df["class_level"] == "SS1"].iloc[0:100]["English Language"],
    c=students_df[students_df["class_level"] == "SS1"].iloc[0:100]["attendance"],
    cmap="viridis"  #color palette
)

#Add labels and title
ax.set_title("Mathematics vs English Language Scores (colored by attendance)")
ax.set_xlabel("Mathematics Scores")
ax.set_ylabel("English Language Scores")


#Add a color bar to show what each colors represent
cbar = plt.colorbar(ax.collections[0], ax= ax)
cbar.set_label("Attendance Rate(%)")

plt.show()