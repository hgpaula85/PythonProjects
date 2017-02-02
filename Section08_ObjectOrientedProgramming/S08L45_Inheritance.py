"""
Object oriented programming
Inheritance
"""

class Car(object):

    def __init__(self):
        print("Just created the car instance")

    def drive(self):
        print("Car started...")

    def stop(self):
        print("Car stopped...")

class BMW(Car):

    def __init__(self):
        Car.__init__(self)
        print("Just created the BMW instance")

print("---","Create Car", "-"*10)
myCar = Car()
myCar.drive()
myCar.stop()

print("\n", "---","Create BMW", "-"*10)
myBmw = BMW()
myBmw.drive()
myBmw.stop()
