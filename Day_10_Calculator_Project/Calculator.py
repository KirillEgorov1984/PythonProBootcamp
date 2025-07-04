def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations["*"](4, 8))

num1 = float(input("What is the first number?: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation: ")
num2 = float(input("What is the next number?: "))
answer = (operations[operation_symbol](num1, num2))
print(f"{num1} {operation_symbol} {num2} = {answer}")