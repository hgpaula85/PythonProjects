"""
Exceptions are errors and we should handle them in our code
Using Else and Finally
"""

def exceptionHandling(a,b,c):
    try:
        d = (a + b) / c
        print(d)
    except ZeroDivisionError:
        print("Zero division error, C cant be zero")

    except TypeError:
        print("Cant add string to integer")

    else:
        print("Else is executed because there was no exception")

    finally:
        print("Finally is always executed")
        
print("---", "Send a string to check TypeError exception", "-"*10)
exceptionHandling(10,"String", 9)

print("\n", "---", "Send zero value to check ZeroDivision exception", "-"*10)
exceptionHandling(10, 5, 0)

print("\n", "---", "Send int values greater than zero and no exception will be displayed", "-"*10)
exceptionHandling(10, 5, 9)