class Vehicle:
    def __init__(self):
        print("super class")
    def drive(self):
        print("Driver are driving")
class Car(Vehicle):
    def __init__(self):
        print("First child class")
        Vehicle.drive(self)
class Bike(Vehicle):
    def __init__(self):
        print("Second child class")
        Vehicle.drive(self)
obj=Car()
obj=Bike()



