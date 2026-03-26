import pandas as pd

df = pd.read_csv("../data/students.csv")

# print(df.isnull().sum()) # used to show how many missing values (NaN0 exist in each column). isnull checks for missing values, .sum() counts the number of true values.

df["Geography"] = df["Geography"].fillna(df["Geography"].mean())

grouped_means = df.groupby('class_level')['Physics'].transform('mean') #calculates average Physics score fro each class level, returns a value for every row.
df['Physics'] = df['Physics'].fillna(grouped_means) # fill missing physics scores using class average

print(grouped_means)