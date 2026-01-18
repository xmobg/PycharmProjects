"""def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

formated_string = format_name("georgi","grozdev")
print(formated_string)"""



def add (n1, n2):
    return n1 + n2
def subtract (n1, n2):
    return n1 - n2
def multiply (n1, n2):
    return n1 * n2
def divide (n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    number_one = float(input("Enter a number: "))
    continue_program = True
    while continue_program:

        for symbol in operators:
            print(symbol)
        operator_one = input("Enter a operator: ")
        number_two = float(input("Enter a number: "))
        answer = operators[operator_one](number_one, number_two)
        print(f"{number_one} {operator_one} {number_two} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start again: ")
        if choice == 'y':
         number_one = answer
        else:
            continue_program = False
            print("\n" * 20)
            calculator()
calculator()