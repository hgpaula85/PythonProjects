"""
Built-in function - creates a sequence of numbers but does not save them in memory
Very useful for generating numbers
"""

my_range = range(0, 20, 2)
print(my_range)
print(type(my_range))
print(list(my_range))

for num in range(0, 21, 2):
    print(num)