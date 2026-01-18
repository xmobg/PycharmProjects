number = int(input())
numbers = 0
while True:
    command = int(input())
    numbers += command
    if numbers >= number:
        print(numbers)
        break