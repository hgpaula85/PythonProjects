"""
Nested dictionary
d = {'k1': {'nestk1':'nestvalue1', 'nestk2': 'nestvalue2'}}
d['k1']['nestk1']
"""

# Define a nested dictionary and print it
print('-'*3, 'Working with nested dictionaries', '-'*10)
cars = {'bmw': {'model': '550i', 'year': 2016}, 'benz': {'model': 'E350', 'year': 2015}}
print('Define nested dictionary:',cars)

bmw_year = cars['bmw']['year']
print('BMW year on dictionary:', bmw_year)

print('Benz model on dictionary:', cars['benz']['model'])