import art

def add(n1, n2):
    return n1 + n2
# TODO write out the other 3 function -subtract,multiple and divide
def subtract(n1,n2):
    return  n1 - n2
def multiple(n1,n2):
    return  n1 * n2
def divide(n1,n2):
    return  n1 / n2
# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

operations = {
    '+': add,
    '-': subtract,
    '*': multiple,
    '/': divide,
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input('What is the first number'))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operations_symbol = input('Pick an operation')
        num2 = float(input('What is the next number'))
        # print(num1+num2)
        answer = operations[operations_symbol](num1,num2)
        print(f'{num1} {operations_symbol} {num2} = {answer}')
        choice = input(f"Type 'Y' to continue calculating with {answer}, or "
              f"type 'n' to start new calculation: ")
        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print('\n'*20)
            calculator()

calculator()