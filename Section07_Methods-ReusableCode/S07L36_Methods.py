"""
A group of code statements which can perform specific task
Methods are reusable and can be called when needed in the code
"""


# Define a method to sum 2 numbers
def sum_nums(n1, n2):
    """
    Get sum of two numbers
    :param n1: integer number
    :param n2: integer number
    :return: Sum of n1 and n2
    """
    return n1 + n2


print('-' * 3, 'Sum two number using a method', '-' * 10)
sum1 = sum_nums(2, 8)
print('2 + 8 using a method:', sum1)

sum2 = sum_nums(3, 3)
print('3 + 3 using a method:', sum2)

print('-' * 3, 'Sum two strings using a method', '-' * 10)
string_add = sum_nums('one', 'two')
print(string_add)


# Define a method to check if the value is on the list
def isMetro(city):
    """
    Check if the value is on the list
    :param city: City
    :return: True or False
    """
    City_List = ['SFo', 'NYC', 'LA']
    if city in City_List:
        return True
    else:
        return False

print('-' * 3, 'Check if value is on the list using a method', '-' * 10)
x = isMetro('boston')
print('Is boston on the list?', x)

x = isMetro('NYC')
print('Is NYC on the list?', x)