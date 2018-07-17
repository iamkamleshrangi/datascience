import pandas as pd

csv_data = pd.read_csv('sample.csv')

# Give the head of csv 
print(csv_data.head())

# return the tail of the csv 
print(csv_data.tail())

# Return the shape of the csv
print(csv_data.shape)

# Return the columns of the csv file
print(csv_data.columns)

# Return the info the csv file 
print(csv_data.info())

# Return 
print('-' * 50)
print(csv_data.database)
print(csv_data.database.value_counts(dropna = False))
