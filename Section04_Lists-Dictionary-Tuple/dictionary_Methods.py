"""
Some methods to handle Dictionaries
"""

print('-'*3, 'Some methods to work with dictionaries', '-'*10)

# Define two dictionaries and print them
car = {'make':'bmw', 'model':'550i', 'year':2016}
cars = {'bmw': {'model': '550i', 'year': 2016}, 'benz': {'model': 'E350', 'year': 2015}}
print('Simple dictionary Car:',car)
print('Nested dictionary Cars:',cars)

# KEYS - Return dictionary keys
print('Simple',car.keys())
print('Nested ',cars.keys())

# VALUES - Return dictionary values
print('Simple', car.values())
print('Nested', cars.values())

# ITEMS - Return dictionary keys and values
print('Simple', car.items())
print('Nested', cars.items())

# COPY - Copy an entire dictionary
car_copy = car.copy()
print('Copy of car simple dictionary', car_copy)

# POP - Remove specific value of dictionary
car.pop('model')
print('Simple', car.items())