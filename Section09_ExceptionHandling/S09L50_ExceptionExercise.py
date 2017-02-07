"""
Create a dictionary CAR
Create 3 keys (make, model, year)
Try to access the color key, as we never created color key
it will throw an exception
"""

def carException():
    try:
        dic_car = {'make': 'BMW', 'model': '550i', 'year':'2017'}
        print(dic_car['color'])

    except:
        print("There is no COLOR key to access")

    finally:
        print("Show this anyway")

print("---", "Try access color key not defined", "-"*10)
carException()