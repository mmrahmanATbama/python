#from art import logo


# Calculator:
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

#print(logo)


def calculator():
    num1 = float(input("What's the first number? "))

    for ops in operations:
        print(ops)
    answer = 'y'
    while answer != 'n':
        operations_symbol = input("Pick an operation : ")
        num2 = float(input("What's the next number? "))

        operator = operations[operations_symbol]
        result = operator(num1, num2)
        print(f" {num1} {operations_symbol} {num2} = {result}")
        num1 = result
        answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation. \nAny other letter to exit: ")
        if answer == 'n':
            calculator()
        elif (answer != 'y' or answer != 'n'):
            quit()

calculator()
