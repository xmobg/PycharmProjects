# Create a function to: Count how many odd numbers are there in a list passed as a parameter

def odd_number_in_list():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    count = 0
    for number in numbers:
        if number % 2 != 0:
            count += 1
    print(f"Odd numbers in list: {count}")

odd_number_in_list()
