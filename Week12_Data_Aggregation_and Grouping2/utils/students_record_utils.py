import pandas as pd
def load_student_records(filename: str) -> pd.DataFrame:
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

