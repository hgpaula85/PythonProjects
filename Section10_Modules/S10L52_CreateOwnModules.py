"""
Import a method from an external module created by me
"""

from modulesexternal import car
from modulesexternal.car import info

class ModulesDemo():

    def car_description(self):
        make = "BMW"
        model = "550i"
        car.info(make, model)

m = ModulesDemo()
m.car_description()