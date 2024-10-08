# Make functions for the mathematical operations
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Store all the above functions in a dictionary
operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}


def calculator():
    """ Asks from the user to choose two numbers and an operation and then gives the result """


should_accumulate = True
num1 = float(input("Type the first number: "))

while should_accumulate:
    for symbol in operations:
        print(symbol)
    oper = input("Choose a mathematical operator: ")
    num2 = float(input("Type the second number: "))

    result = operations[oper](num1, num2)
    print(num1, oper, num2, "=", result)

    # Asks user if they want to continue with the previous result or no
    cont = input(f"Do you want to continue with the previous {result}? y on n: ")
    if cont == "y":
        num1 = result
    else:
        should_accumulate = False
        calculator()

calculator()