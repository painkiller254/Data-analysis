import pandas as pd
import numpy as np

data = np.array(['O', 'S', 'S', 'A'])
S1 = pd.Series(data) # Without adding index
S2 = pd.Series(data,index=[100,101,102,103]) # With adding index 
print(S1) 
print("\n") 
print(S2)

my_series2 = np.random.randn(5, 10)
print("\nmy_series\n", my_series2)

# creating an indexed series

data = {'X': 0., 'Y': 1., 'Z': 2.}
SERIES = pd.Series(data, index=['Y','Z','W','X'])
print(SERIES)

# creating a series using sclara
import pandas as pd
import numpy as np
Sories1 = pd.Series(7, index=[0,1,2,3,4])
print(Sories1)

# Accessing data from a series with a position
import pandas as pd
Series1 = pd.Series([1,2,3,4,5], index = ['a','b','c', 'd', 'e'])
print("Example 1:Retrieve the first element")
print(Series1[0])
print ("\nExample 2:Retrieve the first three element")
print (Series1[:3])
print ("\nExample 3:Retrieve the last three element")
print(Series1[-3:])
print ("\nExample 4:Retrieve a single element")
print (Series1['a'])
print ("\nExample 5:Retrieve multiple elements")
print (Series1[['a','c','d']])


# Analyzing Series Data
my_series1 = pd.Series([5, 6, 7, 8, 9, 10])
print("my_series1\n", my_series1)
print("\n Series Analysis\n")
print("Series mean value :", my_series1.mean()) # find mean value in a series
print("Series max value : ", my_series1.max()) # find max value in a series
print("Series min value : ",my_series1.min())
print("Series standard deviation value : ", my_series1.std())

print(my_series1.describe())

# copying a Series to Another with a reference

my_series_11 = my_series1
print(my_series1)
my_series_11.index = ['A', 'B', 'C', 'D', 'E', 'F']
print(my_series_11)
print(my_series1)

# copying series values to another
print(my_series1)
my_series_11.index = ['A', 'B', 'C', 'D', 'E', 'F']
print(my_series_11)
print(my_series1)

# Operations on a series
print('F' in my_series_11)

temp = my_series_11 < 8
print(temp)

temp = my_series_11[my_series_11 < 8] * 2
print(temp)

# function to add two series and call the function

def AddSeries(x,y):
    for i in range(len(x)):
        print(x[i] + y[i])

print("Add two series\n")
AddSeries(my_series_11, my_series1)

# Visualizing data series
import matplotlib.pyplot as plt
plt.plot(my_series2)
plt.ylabel('index')
plt.show()

from numpy import *
import math
import matplotlib.pyplot as plt
t = linspace(0, 2*math.pi, 400)
a = sin(t)
b = cos(t)
c = a + b

plt.plot(t, a, 'r')
plt.plot(t, b, 'b')
plt.plot(t, c, 'g')
plt.show()
