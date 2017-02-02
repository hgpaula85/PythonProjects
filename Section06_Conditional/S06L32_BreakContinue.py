"""
Break: to break out of the closest enclosing loop
Continue: go to the start of the closest enclosing loop
"""
# Example of BREAK
# print('-'*3, ('Example of BREAK'), '-'*20)
# x = 0
# while x < 10:
#     print('Value of x is', str(x))
#     x = x + 1
#
#     if x == 8:
#         break
#
#     print('Just an example')
#     print('-'*20)
#
# else:
#     print('Just finished or never entered the loop')
#
# print('Just broke out of the loop')

# Example of CONTINUEprint('-'*3, 'Example of CONTINUE', '-'*20)

x = 0
while x < 10:
    print('Value of x is',str(x))
    x = x + 1

    if x == 8:
        continue #here it goes to line 26 (while)

    print('-'*20)

else:
    print('Just finished or never entered the loop')

print('Just broke out of the loop')