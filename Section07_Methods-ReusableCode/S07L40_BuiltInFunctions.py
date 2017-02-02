"""
Some built-in functions

max(): It takes any number of arguments and returns the largest one
min(): It takes any number of arguments and returns the smallest one
abs(): It returns the absolute value of the number, that number's distance from 0.
type(): It returns the type of the data it receives as an argument
"""

# MAX
def largest_num(*nums):
    print(max(nums))
    return(max(nums))

print("--- MAX", "---"*10)
largest_num(-10,-20,100,0,10)

# MIN
def smallest_num(*nums):
    print(min(nums))

print("--- MIN", "---"*10)
smallest_num(-10,-20,100,0,10)

# ABS
def abs_func(a):
    print(abs(a))

print("--- ABS", "---"*10)
abs_func(-10)

# TYPE
print("--- TYPE", "---"*10)
print(type(99))
print(type(99.9))
print(type("99.9"))
list1 = [1,2,3,4]
print(type(list1))