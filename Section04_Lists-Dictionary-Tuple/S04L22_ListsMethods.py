"""
Some methods to handle lists
"""

# Define a list of three cars an print it
print('-'*3, 'List of 3 cars', '-'*10)
cars = ["bmw", "honda", "audi"]
print(cars)

# LEN - Check the lenght of the list and print it
lenght = len(cars)
print('This is the lenght of the list:', lenght)

# APPEND - adds another item at the end of the list
cars.append("Benz")
print('List after appends a new item:', cars)

# INSERT - adds another item at the index we set
cars.insert(1, 'Jeep')
print('List after add item at index 2:', cars)

# INDEX - returns index based on specified value
x = cars.index('honda')
print('This is the index of value Honda:',x+1)

# POP - remove last item on the list
y = cars.pop()
print('This is the item removed from the original list:',y)
print('List with last item removed:',cars)

# Remove - Remove a specified value of the list
cars.remove('Jeep')
print('List with item Jeep removed:',cars)

# Create a new list with parts of the original list
slicing = cars[0:2] #0 is inclusive, 2 is not inclusive
slicing2 = cars[1:]
print('New list with index values from 1 to 2:',slicing)
print('New list with index values from 2 to the end:',slicing2)

# SORT - Sort list alphabetically
print("Original list:",cars)
cars.sort()
print("Sorted list:",cars)