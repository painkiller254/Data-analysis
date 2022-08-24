# pandas.Panel(data, items, majpor_axis, minor_axis, dtype, copy)

# Creating an empty panel
import pandas as pd
import numpy as np

data = np.random.rand(2,4,5)
Paneldf = pd.Panel(data)
print(Paneldf)

# Accessing Data from a Panel with a position
# Selecting and Displaying Panel Items

data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
        'Item2' : pd.DataFrame(np.random.randn(4, 2))
        }

Paneldf = pd.Panel(data)
print(Paneldf['Item1'])
print("\n")
print(Paneldf['Item2'])

# major and minor dimensions'
print(Paneldf.major_xs(1))
print(Paneldf.minor_xs(1))


