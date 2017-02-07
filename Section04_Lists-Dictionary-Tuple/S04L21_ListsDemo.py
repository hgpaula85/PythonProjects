"""
Data type to store more than one value in one variable name
List items are in brackets, separated with "," [1,2,3]
"""

# Define a list of 3 cars, an empty list and print them
print('-' * 3, 'List of 3 cars', '-' * 10)
cars = ['BMW', 'Honda', 'Audi']
empty_list = []
print('This is my list of 3 cars: ', cars)
print('This is my empty list: ', empty_list)
print('This is my second item on the list: ', cars[1])
cars[2] = "Nissan"
print('Item number 3 changed to: ', cars[2])
print('This is my mew list of 3 cars: ', cars)
print('-' * 30)

# Define a numeric list test a sum and print it
print()
print('-' * 3, 'Numeric list', '-' * 10)
num_list = [5, 7, 13]
print('This is my numeric list: ', num_list)
sum_num = num_list[1] + num_list[2]
print('Sum items 2 and 3: ', sum_num)
print('-' * 30)