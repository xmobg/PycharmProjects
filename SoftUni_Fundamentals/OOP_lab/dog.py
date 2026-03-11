class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"Dog {self.name} is barking")

dog1 = Dog("Rudi",1)
dog1.bark()