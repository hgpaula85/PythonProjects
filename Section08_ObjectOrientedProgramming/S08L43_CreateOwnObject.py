"""
Object Oriented Programming
Creating my own object
"""

class Car(object):

    def __init__(self, make, model='550i'):
        self.make = make
        self.model = model

c1 = Car('bmw')
print(c1.make, c1.model)

c2 = Car('benz', 'E350')
print(c2.make, c2.model)