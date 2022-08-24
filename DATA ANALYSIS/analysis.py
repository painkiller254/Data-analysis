import numpy as np
import pandas as pd

Number = [1,2,3,4,5,6,7,8,9,10]
Names = ['Ali Ahmed','Mohamed Ziad','Majid Salim','Salwa Ahmed', 'Ahlam Mohamed', 'Omar Ali', 'Amna Mohammed','Khalid Yousif', 'Safa Humaid', 'Amjad Tayel']
City = ['Fujairah','Dubai','Sharjah','AbuDhabi','Fujairah','Dubai', 'Sharja ', 'AbuDhabi','Sharjah','Fujairah']
columns = ['Number', 'Name', 'City' ]
dataset= pd.DataFrame({'Number': Number , 'Name': Names, 'City': City}, columns = columns )
Gender= pd.DataFrame({'Gender':['Male','Male','Male','Female', 'Female', 'Male', 'Female', 'Male','Female', 'Male']})
Height = pd.DataFrame(np.random.randint(120,175, size=(12, 1))) 
Weight = pd.DataFrame(np.random.randint(50,110, size=(12, 1)))

dataset.groupby('City')['Gender'].count()

print(dataset.groupby('City').groups)

print(dataset.groupby(['City', 'Gender']).groups)

grouped = dataset.groupby('Gender')
for name, group in grouped:
    print(name)
    print(group)
    print("\n")

print(grouped.get_group('Female'))

# Aggregations
grouped = dataset.groupby('Gender')
print(grouped['Height'].agg(np.mean))
print("\n")
print(grouped['Weight'].agg(np.mean))
print("\n")
print(grouped.agg(np.size))
print("\n")
print(grouped['Height'].agg([np.sum, np.mean, np.std]))


# Transformations
dataset = dataset.set_index(['Number'])
print(dataset)


grouped = dataset.groupby("Gender")
score = lambda x: (x - x.mean()) / x.std()*10
print(grouped.transform(score))


# Filtration
print(dataset.groupby('City').filter(lambda x: len(x) >= 3))