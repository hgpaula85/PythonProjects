"""
Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are string, list, tuple and dictionary
"""

# FOR loop to change a to A in a string
print('-'*3, 'Change a to A in a string', '-'*10)
my_string = 'abcabc'
print('Original string:', my_string)

for c in my_string:
    if c == 'a':
        print('A', end=' ')
    else:
        print(c, end=' ')
print()

# FOR loop to change a to A in a list
print('-'*3, 'Change b to B in a list', '-'*10)
my_list = ['a', 'b', 'c', 'a', 'b', 'c']
print('Original list:', my_list)

for c in my_list:
    if c == 'b':
        print('B', end=' ')
    else:
        print(c, end=' ')
print()

# FOR loop to multiply a value by ten in a numeric list
print('-'*3, 'Multiply a value by ten in a numeric list', '-'*10)
my_num_list = [1,2,3,4,5,6,7]
print('Original list:', my_num_list)

for num in my_num_list:
    print(num * 10, end=' ')
print()

# FOR loop to access values in a dictionary
print('-'*3, 'Access values in a dictionary', '-'*10)
my_d = {'one':1, 'two':2, 'three':3}
print('Original dictionary:', my_d.items())

for my_key in my_d:
    print('Key:',my_key, '| Value:',str(my_d[my_key]))

print('-'*3, 'Another example', '-'*10)
for my_key, my_value in my_d.items():
    print('Key:', my_key)
    print('Value:', my_value)