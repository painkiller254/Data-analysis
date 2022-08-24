#DataFrame(data, index, columns, dtype, copy)
# Creating a dataframe from a list

from os import close
import pandas as pd

# data = [10, 20, 30, 40, 50]
# DF1 = pd.DataFrame(data)
# print(DF1)

# data = [['Ossama', 25], ['Ali', 43],['Ziad',32]]
# DF1 = pd.DataFrame(data,columns=['Name', 'Age'])
# print(DF1)

# DF1 = pd.DataFrame(data,columns=['Name', 'Age'], dtype=float)
# print(DF1)


# # Creating a DataFrame from a Dictionary

# data = [{'Test1': 10, 'Test2':20}, {'Test1': 30}, {'Test2': 20, 'Project': 20}]

# # With three column indeices, values same as dictionary keys
# df1 = pd.DataFrame(data, index=['First', 'Second'], columns=['Test2', 'Project', 'Test1'])

# # With two column indices with one index with another name
# df2 = pd.DataFrame(data, index=['First', 'Second'], columns=['Project', 'Test_1','Test2'])

# print(df1)
# print("\n")
# print(df2)

# Creating a dataframe from a series
data = {'Test1' : pd.Series([70, 55, 89], 
        index=['Ahmed', 'Omar', 'Ali']),
        'Test2' : pd.Series([56, 82, 77, 65], 
        index=['Ahmed', 'Omar', 'Ali', 'Salwa'])}

df1 = pd.DataFrame(data)
# print(df1)

# column selection
print(df1['Test2'])
print("\n")
print(df1[:])

print("-" * 20)
# row selction
print(df1.iloc[:, [1,0]])

print(df1[0:4:1])

# Column Addition
# add a new column
df1['Project'] = pd.Series([90,83,67, 87],
index=['Ali', 'Omar', 'Salwa', 'Ahmed'])
print("\n")

df1['Average'] = round((df1['Test1']+df1['Test2']+df1['Project'])/3, 2)
print(df1)

# Column Deletion
df2 = df1
print(df2)
print("Deleting the first column using DEL function:")
# del df2['Test 2']
# print(df2)

df2.pop('Project')
print(df2)



