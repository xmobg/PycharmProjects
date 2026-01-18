your_name = input("Enter your name: ")


def greeting(name):
    print("Hello, " + name + "!")
    print("How are you, " +name + "?")
    print("Good bye!")
greeting(your_name)
#position argument
def greet_with(name,location):
    print(f"Hello, {name}!")
    print(f"What is {location}?")
    print("Good bye!")
greet_with("Georgi","Dobrich")
#keyword argument
def say_hi(name = "Georgi", location = "Dobrich",pets = "fish"):
    print(f"Hello, {name}!")
    print(f"What is {location}?")
    print(f"I have pets, {pets}?")
say_hi()