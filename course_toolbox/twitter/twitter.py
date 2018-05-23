# Import pandas
import pandas as pd

""" We have twitter csv about some interesting facts like which language they use on twitter handler so we collect the
data and put into the program and count the number. That is fun to have .. at the end we calculate the most perfered
language on the twitter """
# Import Twitter data as DataFrame: df
df = pd.read_csv('tweets.csv')

# Initialize an empty dictionary: langs_count
langs_count = dict()

# Extract column from DataFrame: col
col = df['lang']

# Iterate over lang column in DataFrame
for entry in col:

    # If the language is in langs_count, add 1
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1

# Print the populated dictionary
print(langs_count)

