# Exploring and Analyzing a Data Frame

# DataFrame.describe(percentiles=None, include=None, exclude=None)
# [source]

import pandas as pd
import numpy as np

data = {'Age' : pd.Series([30, 25, 44, ], 
index=['Ahmed', 'Omar', 'Ali']),
'Salary' : pd.Series([25000, 17000, 30000, 12000],
index=['Ahmed', 'Omar', 'Ali',]), 
'Height' : pd.Series([160, 154, 175, 165], 
index=['Ahmed', 'Omar', 'Ali', 'Salwa']),
'Weight' : pd.Series([85, 70, 92, 65], index=['Ahmed', 'Omar', 
'Ali', 'Salwa']),
'Gender' : pd.Series(['Male', 'Male', 'Male', 'Female'], 
index=['Ahmed', 'Omar'])}

data = pd.DataFrame(data)
print(data)
print("\n")
df2 = pd.DataFrame([[42, 31000, 170, 80, 'Female']], columns=['Age', 'Salary', 'Height'], index=['Mona'])

data = data.append(df2)
print(data)

# Analyzing a dataframe
data.describe()

data.describe(include="all")

data.Salary.describe()

data.describe(include=[np.number])

data.describe(include=[np.object])

data.describe(exclude=[np.number])

data

OptimalWeight = data['Height'] - 100
print(OptimalWeight)

unOptimalCases = data['Weight'] <= OptimalWeight
print(unOptimalCases)

