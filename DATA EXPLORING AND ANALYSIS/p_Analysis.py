import pandas as pd
import numpy as np

data1 = {'Age' : pd.Series([30, 25, 44, ], index=['Ahmed', 
'Omar', 'Ali']),
'Salary' : pd.Series([25000, 17000, 30000, 12000], 
index=['Ahmed', 'Omar', 'Ali', 'Salwa']),
'Height' : pd.Series([160, 154, 175, 165], index=['Ahmed', 
'Omar', 'Ali', 'Salwa']),
'Weight' : pd.Series([85, 70, 92, 65], index=['Ahmed', 'Omar', 
'Ali', 'Salwa']),
'Gender' : pd.Series(['Male', 'Male', 'Male', 'Female'], 
index=['Ahmed', 'Omar', 'Ali', 'Salwa'])}
data2 = {'Age' : pd.Series([24, 19, 33,25 ], index=['Ziad', 
'Majid', 'Ayman', 'Ahlam']),
'Salary' : pd.Series([17000, 7000, 22000, 21000], 
index=['Ziad', 'Majid', 'Ayman', 'Ahlam']),
'Height' : pd.Series([170, 175, 162, 177], index=['Ziad', 
'Majid', 'Ayman', 'Ahlam']),
'Weight' : pd.Series([77, 84, 74, 90], index=['Ziad', 'Majid', 
'Ayman', 'Ahlam']),
'Gender' : pd.Series(['Male', 'Male', 'Male', 'Female'], 
index=['Ziad', 'Majid', 'Ayman', 'Ahlam'])}

data = {'Group1': data1, 'Group2': data2}
p = pd.Panel(data)

p['Group1'].describe()

p['Group1']['Salary'].describe()

