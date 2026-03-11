class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        return "eat"

class Dog(Animal):
    def bark(self):
        return "bark"

class Cat(Animal):
    def eat(self):
        return "cat eats fish"

    def meow(self):
        return "meow meow"
class bird(Animal):
    def move(self):
        return "flying"
class Fish(Animal):
    def move(self):
        return "swimming"
animals = [bird("Gogo"),Fish("Cveti")]

for animal in animals:
    print(animal.move())
