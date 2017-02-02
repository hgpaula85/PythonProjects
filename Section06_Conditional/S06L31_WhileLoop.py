"""
Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are string, list, tuple and dictionary
"""

print('-'*3, 'This is our first While', '-'*10)
x = 0
while x < 10:
    print('Value of x is:', str(x))
    x = x + 1

print('-'*3, 'Using a While to create a list', '-'*10)
first_list = []
num = 0
while num < 10:
    first_list.append(num)
    print('Value of num:',str(num))
    num += 1

print('List created:', first_list)