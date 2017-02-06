"""
Exercise
Create a class Fruit
Define 3 methods in this class (init, nutrition, fruit_shape)
Print anything in these methods

Create one more class (any fruit name)
Inherit from Fruit class (it will be a child class)
Define 3 methods in this class (init, nutrition and color)
Print anything you like in these methods

Create instances of these classes and call methods from them
Call methods from the base class using an instance of the child class
"""

# Create a class Fruit and 3 methods
class Fruit(object):
    def __init__(self):
        print("This is my Fruit")

    def nutrition(self):
        print("Fruit nutrition")

    def fruit_shape(self):
        print("Fruit shape")

# Create fruit name class
class Apple(Fruit):
    def __init__(self):
        print("This is an apple")

    def nutrition(self):
        super(Apple, self).nutrition()
        print("Apple nutrition")

    def color(self):
        print("Apple color is green")

# Create instances and call methods from parent class
print("---","Parent class", "-"*10)
orange = Fruit()
orange.nutrition()
orange.fruit_shape()

# Call methods from parent and child classes
print("---","Child class", "-"*10)
one_apple = Apple()
one_apple.nutrition()
one_apple.fruit_shape()
one_apple.color()