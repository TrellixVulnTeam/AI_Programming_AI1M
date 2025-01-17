import pandas as pd

groceries = pd.Series(data=[36, 6, 'Yes', 'No'],
                      index=['egss', 'apples', 'milk', 'bread'])
print(groceries)

# We print some information about Groceries
print('Groceries has shape: ', groceries.shape)
print('Groceries has dimension: ', groceries.ndim)
print('Groceries has a total of ', groceries.size, ' elements')

# We print the index and data of Groceries
print('The data in Groceries is: ', groceries.values)
print('The index of Groceries is: ', groceries.index)

# We check whether bananas is a food item (an index) in Groceries
x = 'bananas' in groceries

# We check whether bread is a food item (an index) in Groceries
y = 'bread' in groceries

# We print the results
print('Is bananas an index label in Groceries:', x)
print('Is bread an index label in Groceries:', y)
