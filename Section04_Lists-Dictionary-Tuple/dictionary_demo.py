"""
Data type to store more than one value in one variable name, in terms of key value pairs
Dictionary items are in brackets {} in key:value pairs, separated with ":". Example: {'k1':'v1', 'k2':'v2'}
Not sequenced, no indexing, just mapping
"""

# Define a dictionary an print it
print('-'*3,'My dictionary', '-'*10)
car = {'make':'bmw', 'model':'550i', 'year':2016}
print('Dictionary:',car)

# Define a variable and assign one value from dictionary
model = car['model']
print('Value of key model from dictionary:',model)

# Define an empty dictionary and add values to it
d={}
print('New empty dictionary:',d)
d['one'] = 1
print('First value added:', d)
d['two'] = 2
print('Second value added', d)

# Math operations with values from dictionaryy
sum_1 = d['two'] + 8
print("Sum key value two and 8:",sum_1)

# Math operations and changing value from dictionary
print('Original dictionary:',d)
d['two'] = d['two'] + 8
print('Key value two changed:',d)