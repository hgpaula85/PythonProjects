"""
Object oriented programming
Inheritance - Overriding
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

    def drive(self):
        print("You are driving a BWM now")

    def stop(self):
        super(BMW, self).stop()
        print('You are stopping a BMW')

    def headup_display(self):
        print("This is a unique feature")

print("---","Create Car", "-"*10)
myCar = Car()
myCar.drive()
myCar.stop()

print("\n", "---","Create BMW", "-"*10)
myBmw = BMW()
myBmw.drive()
myBmw.stop()
myBmw.headup_display()