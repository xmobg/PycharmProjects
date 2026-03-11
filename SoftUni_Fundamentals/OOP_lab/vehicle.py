class Vehicle:
    def __init__(self, brand,speed):
        self.brand = brand
        self.speed = speed
    def move(self):
        return f"Vehicle moving at {self.speed} km/h"

class Plane(Vehicle):
    def move(self):
        return f"Plane {self.brand} moving at {self.speed} km/h"

class Car(Vehicle):
    def move(self):
        return f"Car {self.brand} moving at {self.speed} km/h"

vechicle = [
    Car("BMW",140),
    Plane("MIG-29",600)
]
for vechicle in vechicle:
    print(vechicle.move())