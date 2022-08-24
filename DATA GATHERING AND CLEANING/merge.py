# Merging and Intergrating Data
# an explicit example

import pandas as pd

a = pd.read_csv("1. Export1_Columns.csv")
b = pd.read_csv("1. Export2_Columns.csv")

a.head()
b.head()

b.drop('2014', axis=1, inplace=True)
columns = ['2013', '2012']
b.drop(columns, iplace=True, axis=1)
b.head()

mergedDataSet = a.merge(b, on="Country Name")
mergedDataSet.head()

dataX = a.merge(b)
dataX.head()

Data1 = a.head()
Data1=Data1.reset_index()
Data1

Data2 = a.tail()
Data2=Data2.reset_index()
Data2

VerticalStack = pd.concat((Data1, Data2), axis=0)
VerticalStack
