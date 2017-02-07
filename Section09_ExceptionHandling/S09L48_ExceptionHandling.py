"""
Exceptions are errors and we should handle them in our code to make
sure the code is working the way we want and is handling all the unwanted issues
https://docs.python.org/3/library/exceptions.html
"""

def exceptionHandling(a,b,c):
    try:
        d = (a + b) / c
        print(d)
    except ZeroDivisionError:
        print("Zero division error, C cant be zero")

    except TypeError:
        print("Cant add string to integer")

print("---", "Send a string to check TypeError exception", "-"*10)
exceptionHandling(10,"String", 9)

print("\n", "---", "Send zero value to check ZeroDivision exception", "-"*10)
exceptionHandling(10, 5, 0)

print("\n", "---", "Send int values greater than zero and no exception will be displayed", "-"*10)
exceptionHandling(10, 5, 9)