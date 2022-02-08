def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide
}

def calculator():
    num1 = float(input('What is the first number?: '))

    for each_symbol in operations:
            print(each_symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input('Pick an operation: ')
        num2 = float(input('What is the next number?: '))
        calculation = operations[operation_symbol]
        answer = round(calculation(num1, num2), 1)

        print(f'{num1} {operation_symbol} {num2} = {answer}')

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new the calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator() 
    
