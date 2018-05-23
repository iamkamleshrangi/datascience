# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

## Data set of CSV files
#     cars_per_cap        country drives_right
#US            809  United States         True
#AUS           731      Australia        False
#JAP           588          Japan        False
#IN             18          India        False
#RU            200         Russia         True
#MOR            70        Morocco         True
#EG             45          Egypt         True

# Print out drives_right column as Series
print(cars.iloc[:,2])

# Print out drives_right column as DataFrame
print(cars.loc[:,['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])
