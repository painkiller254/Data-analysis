"""
1. acquisition
2. cleaning
3. Explatory
4. analysis
5. visualization

numpy
pandas
matplotlib
scipy
"""

import pandas as pd
import numpy as np

dataset = pd.DataFrame(np.random.randn(5, 3), 
index=['a', 'c', 'e', 'f', 'h'], columns=['stock1', 'stock2', 'stock3'])
dataset.rename(columns={"one":'stock1', "two":"stock2", "three":'stock3'}, inplace=True)

dataset = dataset.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

# print(dataset)
# print(dataset['stock1'].isnull())
first = dataset.fillna(0)
sec = dataset.fillna(method="pad")
thrd = dataset.dropna()
fin = dataset.replace(np.nan, 0)
print(fin)
