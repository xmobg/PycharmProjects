# Create a function to: Find the smallest number in a list passed as a parameter
def smallest_number_in_list():
    numbers = [15,10,5,22,50,60,70,80,90,100]
    smallest_number = numbers[0]
    for number in numbers:
        if number <= smallest_number:
            smallest_number = number
    print(f"Smallest number in list is: {smallest_number}")
smallest_number_in_list()