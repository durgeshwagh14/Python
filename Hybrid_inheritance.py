# 5) Hybrid Inheritance
# A combination of two or more types of inheritance.
class Vehicle:
    def engine(self):
        print("Engine started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")

class NewCar(Car,Bike):
  def new(self):
    print("New Car")

n = NewCar()

n.drive()
n.ride()
n.engine()
n.new()
