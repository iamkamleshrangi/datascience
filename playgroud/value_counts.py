import pandas as pd

csv_data = pd.read_csv('sample.csv')

print(csv_data.columns)
print('--- list value of the column [database] function ---')
print(csv_data.database)
print('--- value count ---')
print(csv_data.database.value_counts(dropna= False))
print('-- describe --')
print(csv_data.describe)
print('-- by [] --')
#print(csv_data['database'].value_counts(dropna = False))
