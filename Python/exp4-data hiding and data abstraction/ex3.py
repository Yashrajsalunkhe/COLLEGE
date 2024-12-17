from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass

class Tesla(Car):
    def mileage(self):
        print("\nThe mileage is 30KmpH")

class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25KmpH")

class Renault(Car):
    def mileage(self):
        print("The mileage is 27KmpH\n")

# Creating objects of each class
t = Tesla()
t.mileage()

s = Suzuki()
s.mileage()

r = Renault()
r.mileage()
