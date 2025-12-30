x = float(input('Enter the first number: '))
print()

oper = input('Enter the operator (+, -, *, /): ')
print()

y = float(input('Enter the second number: '))
print()

if oper == '+':
    result = x + y
elif oper == '-':
    result = x - y
elif oper == '*':
    result = x * y
elif oper == '/':
    if y != 0:
        result = x / y
    else:
        result = 'Error! Division by zero is not allowed.'
print("Result: ", result)