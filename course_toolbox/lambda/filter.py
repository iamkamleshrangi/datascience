# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Use filter() to apply a lambda function over fellowship: result
fellowship = filter(lambda member : len(member) > 6, fellowship)

# Convert result to a list: result_list
result_list = list(fellowship)

# Convert result into a list and print it
print(result_list)

