# import pandas as pd
# sales = pd.read_csv("sales.csv")
# print("\n\n<<<<<<< First 5 records <<<<<<<<\n\n")
# print(sales.head())
# print(sales.tail())

# Reading and cleaning CSV Data
import pandas as pd
salesNrows = pd.read_csv("sales.csv", nrows=4, usecols=[1, 3, 4])
salesNrows.rename(columns={"Country": 'state', "Sales Channel": 'channel', "Order Priority": 'priority'}, inplace=True)

print(len(salesNrows['state'].unique()))
print(salesNrows['state'].unique())

print(salesNrows.isnull())

# function example
def cleanData_sales(cell):
    if (cell=="n.a." or cell=="-1" or cell=="not available"):
        return 0
    return cell

def cleanData_REGION(cell):
    if(cell=="n.a." or cell=="-1" or cell=="not available"):
        return 'AbuDhabi'
    return cell

sales = pd.read_csv('sales.csv', nrows=7, converters={
    "state": cleanData_REGION,
    "channel": cleanData_sales,
    "priority": cleanData_sales,
})

sales.head(20)


